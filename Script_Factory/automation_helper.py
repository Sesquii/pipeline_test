#!/usr/bin/env python3
"""
Automation helper for Script Factory test generation and module conversion.
Converts .txt output files to .py modules and updates test imports.
"""

import os
import shutil
import re
from pathlib import Path

class ScriptFactoryAutomation:
    def __init__(self, base_path=None):
        if base_path is None:
            self.base_path = Path(__file__).parent
        else:
            self.base_path = Path(base_path)
        
        self.runs_dir = self.base_path / "Script_Factory_Runs" / "all_runs"
        self.tests_dir = self.base_path / "Tests"
    
    def convert_txt_to_py(self, txt_file_path):
        """Convert a .txt file to a .py module."""
        txt_path = Path(txt_file_path)
        if not txt_path.exists():
            print(f"Error: {txt_file_path} does not exist")
            return None
        
        # Create .py file path
        py_path = txt_path.with_suffix('.py')
        
        # Copy content from .txt to .py
        shutil.copy2(txt_path, py_path)
        print(f"Converted {txt_path.name} -> {py_path.name}")
        
        return py_path
    
    def ensure_init_files(self):
        """Ensure all necessary __init__.py files exist for proper package structure."""
        init_dirs = [
            self.base_path,
            self.base_path / "Script_Factory_Runs",
            self.base_path / "Script_Factory_Runs" / "all_runs",
            self.base_path / "Tests"
        ]
        
        for dir_path in init_dirs:
            init_file = dir_path / "__init__.py"
            if not init_file.exists():
                init_file.write_text(f"# {dir_path.name} package\n")
                print(f"Created {init_file}")
    
    def fix_test_imports(self, test_file_path, module_name):
        """Fix import statements in test files to use proper module paths."""
        test_path = Path(test_file_path)
        if not test_path.exists():
            print(f"Error: {test_file_path} does not exist")
            return
        
        content = test_path.read_text()
        
        # Fix the import statement - remove .txt extension and fix casing
        old_import_pattern = rf"from Script_Factory\.Script_Factory_runs\.all_runs\.{module_name}\.txt import"
        new_import = f"from Script_Factory.Script_Factory_Runs.all_runs.{module_name} import"
        
        content = re.sub(old_import_pattern, new_import, content, flags=re.IGNORECASE)
        
        # Also fix any other variations
        old_import_pattern2 = rf"from Script_Factory\.Script_Factory_Runs\.all_runs\.{module_name}\.txt import"
        content = re.sub(old_import_pattern2, new_import, content)
        
        test_path.write_text(content)
        print(f"Fixed imports in {test_path.name}")
    
    def process_all_txt_files(self):
        """Process all .txt files in the runs directory."""
        if not self.runs_dir.exists():
            print(f"Error: {self.runs_dir} does not exist")
            return
        
        txt_files = list(self.runs_dir.glob("*.txt"))
        if not txt_files:
            print("No .txt files found in runs directory")
            return
        
        self.ensure_init_files()
        
        for txt_file in txt_files:
            # Convert .txt to .py
            py_file = self.convert_txt_to_py(txt_file)
            if py_file:
                # Find corresponding test file
                module_name = txt_file.stem
                test_file = self.tests_dir / f"test_{module_name}.py"
                
                if test_file.exists():
                    self.fix_test_imports(test_file, module_name)
                else:
                    print(f"Warning: No test file found for {module_name}")
    
    def run_tests(self, test_file=None):
        """Run pytest on specified test file or all test files."""
        import subprocess
        
        if test_file:
            test_path = Path(test_file)
            if not test_path.is_absolute():
                test_path = self.tests_dir / test_file
        else:
            test_path = self.tests_dir
        
        try:
            result = subprocess.run(
                ["python", "-m", "pytest", str(test_path), "-v"],
                cwd=self.base_path.parent,
                capture_output=True,
                text=True
            )
            print("STDOUT:", result.stdout)
            print("STDERR:", result.stderr)
            print("Return code:", result.returncode)
            return result.returncode == 0
        except Exception as e:
            print(f"Error running tests: {e}")
            return False

def main():
    """Main function for command-line usage."""
    import argparse
    
    parser = argparse.ArgumentParser(description="Script Factory Automation Helper")
    parser.add_argument("--convert-all", action="store_true", 
                       help="Convert all .txt files to .py modules")
    parser.add_argument("--convert", type=str, 
                       help="Convert specific .txt file to .py module")
    parser.add_argument("--fix-imports", type=str, 
                       help="Fix imports in specific test file")
    parser.add_argument("--run-tests", type=str, nargs="?", const="all",
                       help="Run tests (specify file or 'all')")
    
    args = parser.parse_args()
    
    automation = ScriptFactoryAutomation()
    
    if args.convert_all:
        automation.process_all_txt_files()
    
    if args.convert:
        automation.convert_txt_to_py(args.convert)
    
    if args.fix_imports:
        # Extract module name from test file name
        test_name = Path(args.fix_imports).stem
        if test_name.startswith("test_"):
            module_name = test_name[5:]  # Remove "test_" prefix
            automation.fix_test_imports(args.fix_imports, module_name)
    
    if args.run_tests:
        if args.run_tests == "all":
            automation.run_tests()
        else:
            automation.run_tests(args.run_tests)

if __name__ == "__main__":
    main()
