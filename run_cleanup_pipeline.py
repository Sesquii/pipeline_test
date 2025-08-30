import sys
import shutil
from pathlib import Path
from datetime import datetime
from basic_cleanup import clean_file

def get_next_run_number(base_dir: Path, cleanup_name: str) -> int:
    """Get the next run number for the given cleanup type"""
    cleanup_dir = base_dir / 'cleanup' / cleanup_name
    if not cleanup_dir.exists():
        return 1
    
    # Find all run directories and get the highest number
    run_dirs = [d for d in cleanup_dir.iterdir() if d.is_dir() and d.name.isdigit()]
    return max([int(d.name) for d in run_dirs], default=0) + 1

def process_directory(source_dir: Path, target_dir: Path, cleanup_func):
    """Recursively process all Python files in source_dir and copy cleaned versions to target_dir"""
    for item in source_dir.iterdir():
        if item.is_dir():
            # Skip the cleanup directory to prevent infinite recursion
            if item.name == 'cleanup':
                continue
            new_target = target_dir / item.name
            new_target.mkdir(exist_ok=True, parents=True)
            process_directory(item, new_target, cleanup_func)
        elif item.suffix == '.py':
            # Create target directory structure
            target_file = target_dir / item.relative_to(source_dir)
            target_file.parent.mkdir(exist_ok=True, parents=True)
            
            # Copy the file
            shutil.copy2(item, target_file)
            
            # Apply cleanup
            try:
                cleanup_func(target_file)
                print(f"Processed: {target_file}")
            except Exception as e:
                print(f"Error processing {target_file}: {e}")

def main():
    if len(sys.argv) < 2:
        print(f"Usage: {sys.argv[0]} <cleanup_script_name>")
        print("Example: python run_cleanup_pipeline.py basic_cleanup")
        sys.exit(1)
    
    cleanup_name = sys.argv[1]
    source_dir = Path('Pytest_scripts')
    
    if not source_dir.exists():
        print(f"Error: Source directory {source_dir} not found")
        sys.exit(1)
    
    # Get the next run number
    run_number = get_next_run_number(source_dir, cleanup_name)
    
    # Create target directory for this run
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    run_dir = source_dir / 'cleanup' / cleanup_name / f"{run_number:03d}_{timestamp}"
    run_dir.mkdir(parents=True, exist_ok=True)
    
    print(f"Starting cleanup run {run_number} using {cleanup_name}")
    print(f"Output directory: {run_dir}")
    
    # Process all Python files
    process_directory(source_dir, run_dir, clean_file)
    
    print("\nCleanup complete!")
    print(f"Processed files are in: {run_dir}")

if __name__ == "__main__":
    main()
