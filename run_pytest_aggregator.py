import os
import re
import json
import time
import subprocess
from pathlib import Path
from collections import defaultdict
from datetime import datetime

class PytestAggregator:
    def __init__(self, test_dir='Pytest_scripts/cleanup', timeout=30):
        self.test_dir = Path(test_dir).absolute()
        self.timeout = timeout
        self.results = {
            'by_batch': defaultdict(lambda: {'total': 0, 'passed': 0, 'failed': 0, 'errors': 0, 'timeout': 0}),
            'by_model': defaultdict(lambda: {'total': 0, 'passed': 0, 'failed': 0, 'errors': 0, 'timeout': 0}),
            'total': {'total': 0, 'passed': 0, 'failed': 0, 'errors': 0, 'timeout': 0}
        }
        self.failed_tests = []
        self.timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        
        # Create output directory
        self.output_dir = Path('misc_pytest_outputs')
        self.output_dir.mkdir(exist_ok=True)
        
        # Set environment variable for test outputs
        import os
        os.environ['PYTEST_OUTPUT_DIR'] = str(self.output_dir.absolute())
    
    def parse_test_filename(self, filepath):
        batch_match = re.search(r'Test_(BATCH\d+)', filepath.name)
        batch = batch_match.group(1) if batch_match else 'unknown_batch'
        
        path_parts = list(filepath.parts)
        model = 'unknown_model'
        model_indicators = ['qwen', 'devstral', 'granite']
        for part in reversed(path_parts):
            if any(indicator in part.lower() for indicator in model_indicators):
                model = part
                break
                
        return batch, model
    
    def run_pytest(self, test_file):
        cmd = ['pytest', str(test_file)]
        
        try:
            start_time = time.time()
            result = subprocess.run(
                cmd,
                capture_output=True,
                text=True,
                timeout=self.timeout
            )
            duration = time.time() - start_time
            
            # Parse the summary line: "======= X failed, Y passed in Z.ZZs ========"
            summary_match = re.search(
                r'=+ (\d+) failed, (\d+) passed in [\d\.]+s =+',
                result.stdout
            )
            
            if summary_match:
                failed = int(summary_match.group(1))
                passed = int(summary_match.group(2))
                return {
                    'status': 'completed',
                    'passed': passed,
                    'failed': failed,
                    'error': None,
                    'duration': duration
                }
            else:
                # If we can't parse the output, log the entire output as an error
                error_msg = "Failed to parse pytest output. "
                if result.stderr:
                    error_msg += f"Stderr: {result.stderr[:200]}..."
                elif result.stdout:
                    error_msg += f"Stdout: {result.stdout[:200]}..."
                else:
                    error_msg += "No output from pytest."
                    
                return {
                    'status': 'error',
                    'passed': 0,
                    'failed': 1,
                    'error': error_msg,
                    'duration': duration
                }
            
        except subprocess.TimeoutExpired:
            return {'status': 'timeout', 'passed': 0, 'failed': 1, 'error': f'Timeout after {self.timeout}s'}
            
        except Exception as e:
            return {'status': 'error', 'passed': 0, 'failed': 1, 'error': str(e)}
    
    def process_test_file(self, test_file):
        batch, model = self.parse_test_filename(test_file)
        print(f"\nTesting: {test_file}")
        print(f"Batch: {batch}, Model: {model}")
        
        result = self.run_pytest(test_file)
        
        # Update results
        self.results['total']['total'] += 1
        self.results['by_batch'][batch]['total'] += 1
        self.results['by_model'][model]['total'] += 1
        
        # Handle different result statuses
        if result['status'] == 'timeout':
            print(f"  ⏱️  Timeout after {self.timeout}s")
            self.results['total']['timeout'] += 1
            self.results['by_batch'][batch]['timeout'] += 1
            self.results['by_model'][model]['timeout'] += 1
            self.failed_tests.append({
                'file': str(test_file),
                'batch': batch,
                'model': model,
                'status': 'timeout',
                'error': result['error'],
                'duration': result.get('duration', 0)
            })
        elif result['status'] == 'error':
            print(f"  ❌ Error: {result['error']}")
            self.results['total']['errors'] += 1
            self.results['by_batch'][batch]['errors'] += 1
            self.results['by_model'][model]['errors'] += 1
            self.failed_tests.append({
                'file': str(test_file),
                'batch': batch,
                'model': model,
                'status': 'error',
                'error': result['error'],
                'duration': result.get('duration', 0)
            })
        else:
            # Successful test run with parsed results
            duration_str = f"{result.get('duration', 0):.2f}s" if 'duration' in result else "N/A"
            print(f"  ✅ Passed: {result['passed']}, ❌ Failed: {result['failed']} in {duration_str}")
            
            # Update passed/failed counts
            self.results['total']['passed'] += result['passed']
            self.results['total']['failed'] += result['failed']
            
            self.results['by_batch'][batch]['passed'] += result['passed']
            self.results['by_batch'][batch]['failed'] += result['failed']
            
            self.results['by_model'][model]['passed'] += result['passed']
            self.results['by_model'][model]['failed'] += result['failed']
            
            if result['failed'] > 0:
                self.failed_tests.append({
                    'file': str(test_file),
                    'batch': batch,
                    'model': model,
                    'status': 'failed',
                    'passed': result['passed'],
                    'failed': result['failed'],
                    'duration': result.get('duration', 0)
                })
    
    def generate_report(self):
        report = []
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        report.append(f"Test Run Report - {timestamp}")
        report.append(f"Generated at: {timestamp}")
        report.append(f"Test directory: {self.test_dir}")
        report.append(f"Output directory: {self.output_dir.absolute()}")
        report.append(f"Timeout per test: {self.timeout} seconds")
        report.append("=" * 80)
        
        # Calculate totals
        total = self.results['total']
        total_tests = total['passed'] + total['failed'] + total['timeout'] + total['errors']
        pass_rate = (total['passed'] / total_tests * 100) if total_tests > 0 else 0
        
        # Summary
        report.append("\n📊 SUMMARY")
        report.append("-" * 80)
        report.append(f"Total test files: {total['total']}")
        report.append(f"✅ Passed: {total['passed']} tests")
        report.append(f"❌ Failed: {total['failed']} tests")
        report.append(f"⚠️  Errors: {total['errors']} tests")
        report.append(f"⏱️  Timeouts: {total['timeout']} tests")
        report.append(f"📈 Pass rate: {pass_rate:.1f}%")
        report.append(f"💥 Failure rate: {((total['failed'] + total['errors'] + total['timeout']) / total_tests * 100):.1f}%" if total_tests > 0 else "")
        
        # By batch
        if self.results['by_batch']:
            report.append("\n📦 RESULTS BY BATCH")
            report.append("-" * 80)
            for batch, stats in sorted(self.results['by_batch'].items()):
                if stats['total'] > 0:
                    batch_total = stats['passed'] + stats['failed'] + stats['timeout'] + stats['errors']
                    passed_pct = (stats['passed'] / batch_total * 100) if batch_total > 0 else 0
                    report.append(
                        f"{batch.ljust(15)} "
                        f"✅ {str(stats['passed']).ljust(4)} "
                        f"❌ {str(stats['failed']).ljust(4)} "
                        f"⚠️  {str(stats['errors']).ljust(4)} "
                        f"⏱️  {str(stats['timeout']).ljust(4)} "
                        f"| {passed_pct:5.1f}%"
                    )
        
        # By model
        if self.results['by_model']:
            report.append("\n🤖 RESULTS BY MODEL")
            report.append("-" * 80)
            for model, stats in sorted(self.results['by_model'].items()):
                if stats['total'] > 0:
                    model_total = stats['passed'] + stats['failed'] + stats['timeout'] + stats['errors']
                    passed_pct = (stats['passed'] / model_total * 100) if model_total > 0 else 0
                    report.append(
                        f"{model.ljust(30)} "
                        f"✅ {str(stats['passed']).ljust(4)} "
                        f"❌ {str(stats['failed']).ljust(4)} "
                        f"⚠️  {str(stats['errors']).ljust(4)} "
                        f"⏱️  {str(stats['timeout']).ljust(4)} "
                        f"| {passed_pct:5.1f}%"
                    )
        
        # Failed tests summary
        if self.failed_tests:
            report.append("\n❌ FAILED TESTS SUMMARY")
            report.append("-" * 80)
            
            # Count failures by status
            status_counts = defaultdict(int)
            for test in self.failed_tests:
                status_counts[test['status']] += 1
            
            # Show counts by status
            report.append("Failed tests by status:")
            for status, count in status_counts.items():
                icon = '⏱️ ' if status == 'timeout' else '⚠️ ' if status == 'error' else '❌ '
                report.append(f"  {icon}{status.title()}: {count}")
            
            # Show counts by batch
            batch_counts = defaultdict(int)
            for test in self.failed_tests:
                batch_counts[test['batch']] += 1
            
            if batch_counts:
                report.append("\nFailed tests by batch:")
                for batch, count in sorted(batch_counts.items()):
                    report.append(f"  {batch}: {count}")
            
            # Show counts by model
            model_counts = defaultdict(int)
            for test in self.failed_tests:
                model_counts[test['model']] += 1
            
            if model_counts:
                report.append("\nFailed tests by model:")
                for model, count in sorted(model_counts.items()):
                    report.append(f"  {model}: {count}")
            
            report.append("\nFor detailed error messages, check the individual test output above.")
        
        # Add execution time
        end_time = time.time()
        execution_time = end_time - time.mktime(datetime.strptime(timestamp, '%Y-%m-%d %H:%M:%S').timetuple())
        report.append(f"\n⏱️  Total execution time: {execution_time:.2f} seconds")
        
        return "\n".join(report)
    
    def save_report(self, report):
        self.output_dir.mkdir(exist_ok=True)
        # Save report to file in output directory
        report_file = self.output_dir / f'test_report_{self.timestamp}.txt'
        with open(report_file, 'w', encoding='utf-8') as f:
            f.write('\n'.join(report))
        print(f"\nReport saved to: {report_file}")
        
        # Also save results as JSON in output directory
        import json
        json_file = self.output_dir / f'test_results_{self.timestamp}.json'
        with open(json_file, 'w', encoding='utf-8') as f:
            json.dump({
                'summary': self.results,
                'failed_tests': self.failed_tests,
                'timestamp': datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
                'test_dir': str(self.test_dir)
            }, f, indent=2)
        print(f"Results saved to: {json_file}")
        
        # Create a symlink to the latest results for easy access
        latest_json = self.output_dir / 'latest_results.json'
        if latest_json.exists():
            latest_json.unlink()
        latest_json.symlink_to(json_file.name)
        print(f"Latest results symlink: {latest_json}")
        
        # Create a README in the output directory
        readme = self.output_dir / 'README.md'
        if not readme.exists():
            with open(readme, 'w') as f:
                f.write("# Pytest Outputs\n\n"
                      "This directory contains test outputs and reports.\n"
                      "- `test_report_*.txt`: Text summary of test results\n"
                      "- `test_results_*.json`: Detailed JSON results\n"
                      "- `latest_results.json`: Symlink to the most recent results\n\n"
                      "## Cleanup\n"
                      "Old files are not automatically removed. You may want to periodically clean up old reports.")
    
    def run(self):
        print(f"Starting test aggregation in: {self.test_dir}")
        print(f"Timeout per test: {self.timeout} seconds\n")
        
        test_files = list(self.test_dir.rglob('Test_*.py'))
        if not test_files:
            print("No test files found!")
            return
            
        print(f"Found {len(test_files)} test files\n")
        
        for test_file in test_files:
            self.process_test_file(test_file)
        
        report = self.generate_report()
        print("\n" + "="*60)
        print(report)
        self.save_report(report)

if __name__ == "__main__":
    import argparse
    
    parser = argparse.ArgumentParser(description='Run pytest on all test files and generate a summary report.')
    parser.add_argument('--dir', default='Pytest_scripts/cleanup', help='Directory containing test files')
    parser.add_argument('--timeout', type=int, default=30, help='Timeout in seconds for each test file')
    
    args = parser.parse_args()
    
    aggregator = PytestAggregator(test_dir=args.dir, timeout=args.timeout)
    aggregator.run()
