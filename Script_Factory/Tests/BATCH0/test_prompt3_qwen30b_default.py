import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))

from Script_Factory.Script_Factory_Runs.all_runs.emotion_file_sorter import (
    get_file_score,
    sort_files,
    print_table,
    move_files
)
import pytest
from pathlib import Path
import tempfile
import shutil
from datetime import datetime, timedelta

def test_get_file_score_positive_words():
    """Test that positive words increase the file score."""
    # Create a temporary directory and file with positive words
    with tempfile.TemporaryDirectory() as tmp_dir:
        test_file = Path(tmp_dir) / "test.txt"
        test_file.write_text("This is a good happy wonderful file with amazing joy.")
        
        score = get_file_score(test_file)
        assert score > 0, "Score should be positive with positive words"

def test_get_file_score_emojis():
    """Test that emojis increase the file score."""
    # Create a temporary directory and file with emojis
    with tempfile.TemporaryDirectory() as tmp_dir:
        test_file = Path(tmp_dir) / "test.txt"
        test_file.write_text("This is a happy file 😀😃😄")
        
        score = get_file_score(test_file)
        assert score > 0, "Score should be positive with emojis"

def test_get_file_score_empty_file():
    """Test that empty files return a score."""
    # Create a temporary directory and empty file
    with tempfile.TemporaryDirectory() as tmp_dir:
        test_file = Path(tmp_dir) / "empty.txt"
        test_file.write_text("")
        
        score = get_file_score(test_file)
        assert isinstance(score, float), "Score should be a float"
        assert score >= 0, "Score should not be negative for empty files"

def test_get_file_score_unreadable_file():
    """Test that unreadable files return penalized score."""
    # Create a temporary directory
    with tempfile.TemporaryDirectory() as tmp_dir:
        test_file = Path(tmp_dir) / "test.txt"
        # Write some content
        test_file.write_text("Some content")
        
        # Make file unreadable by removing read permissions (on Unix-like systems)
        if hasattr(os, 'chmod'):
            os.chmod(test_file, 0o000)
        
        try:
            score = get_file_score(test_file)
            assert score == -100, "Unreadable files should return penalized score"
        finally:
            # Restore permissions for cleanup
            if hasattr(os, 'chmod'):
                os.chmod(test_file, 0o644)

def test_sort_files_basic():
    """Test sorting files by happiness score."""
    with tempfile.TemporaryDirectory() as tmp_dir:
        dir_path = Path(tmp_dir)
        
        # Create test files
        (dir_path / "file1.txt").write_text("This is a happy file 😀")
        (dir_path / "file2.txt").write_text("This is a sad file 😞")
        (dir_path / "file3.txt").write_text("This is an average file")
        
        # Test sorting
        files = sort_files(tmp_dir)
        assert len(files) == 3, "Should find all three files"
        # The first file should have higher score due to emoji
        assert files[0][0] >= files[1][0] >= files[2][0], "Files should be sorted by score descending"

def test_sort_files_empty_directory():
    """Test sorting in an empty directory."""
    with tempfile.TemporaryDirectory() as tmp_dir:
        files = sort_files(tmp_dir)
        assert len(files) == 0, "Should return empty list for empty directory"

def test_print_table_formatting():
    """Test that print_table formats output correctly."""
    # Capture stdout
    import io
    from contextlib import redirect_stdout
    
    sorted_files = [
        (95.5, Path("test1.txt")),
        (80.2, Path("test2.txt"))
    ]
    
    f = io.StringIO()
    with redirect_stdout(f):
        print_table(sorted_files)
    output = f.getvalue()
    
    assert "Score" in output
    assert "Path" in output
    assert "test1.txt" in output
    assert "test2.txt" in output

def test_move_files_dry_run():
    """Test that move_files with dry-run flag doesn't actually move files."""
    with tempfile.TemporaryDirectory() as tmp_dir:
        dir_path = Path(tmp_dir)
        
        # Create a test file
        test_file = dir_path / "test.txt"
        test_file.write_text("Content")
        
        # Get original file path
        original_file = test_file
        
        # This should not actually move the file due to dry run
        move_files([(95.0, test_file)], dry_run=True)
        
        # File should still exist in original location
        assert original_file.exists(), "File should still exist in original location during dry run"

def test_move_files_normal():
    """Test that move_files actually moves files when not in dry-run mode."""
    with tempfile.TemporaryDirectory() as tmp_dir:
        dir_path = Path(tmp_dir)
        
        # Create a test file
        test_file = dir_path / "test.txt"
        test_file.write_text("Content")
        
        # This should move the file to a score-based folder
        sorted_files = [(95.0, test_file)]
        move_files(sorted_files, dry_run=False)
        
        # The file should be moved to a score folder
        score_folders = [d for d in dir_path.iterdir() if d.is_dir() and "score" in d.name]
        assert len(score_folders) >= 1, "Should have created score-based folders"
        # Check that the file was moved (the original should not exist)
        assert not test_file.exists(), "Original file should be moved"

def test_get_file_score_no_extension():
    """Test file score calculation for files with no extension."""
    with tempfile.TemporaryDirectory() as tmp_dir:
        test_file = Path(tmp_dir) / "no_extension"
        test_file.write_text("Some content")
        
        score = get_file_score(test_file)
        assert isinstance(score, float), "Score should be a float"

def test_get_file_score_invalid_path():
    """Test that invalid paths return penalized score."""
    fake_path = Path("/this/path/does/not/exist.txt")
    score = get_file_score(fake_path)
    assert score == -100, "Invalid paths should return penalized score"