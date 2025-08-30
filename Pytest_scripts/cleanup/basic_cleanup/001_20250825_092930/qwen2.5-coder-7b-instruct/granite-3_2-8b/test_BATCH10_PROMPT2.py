#!/usr/bin/env python3

import psutil
from random import choice
from haikus import get_haiku  # You'll need to install this library using pip: pip install haikus


def memory_to_haiku():
    memory = dict(psutil.virtual_memory()._asdict())
    free = f"{memory['free'] / (1024**3):.2f}"  # Convert bytes to GB, format to 2 decimal places
    used = f"{memory['used'] / (1024**3):.2f}"  # Convert bytes to GB, format to 2 decimal places

    lines = [
        f"Memory's vast expanse,",
        f"{choice(['sparse', 'crammed', 'empty', 'packed'])} with {free}.",
        f"A world within my grasp."
    ]

    return "\n".join(lines)


def main():
    haiku = memory_to_haiku()
    print(haiku)


if __name__ == "__main__":
    main()

# ===== GENERATED TESTS =====
#!/usr/bin/env python3

import psutil
from random import choice
from haikus import get_haiku  # You'll need to install this library using pip: pip install haikus


def memory_to_haiku():
    memory = dict(psutil.virtual_memory()._asdict())
    free = f"{memory['free'] / (1024**3):.2f}"  # Convert bytes to GB, format to 2 decimal places
    used = f"{memory['used'] / (1024**3):.2f}"  # Convert bytes to GB, format to 2 decimal places

    lines = [
        f"Memory's vast expanse,",
        f"{choice(['sparse', 'crammed', 'empty', 'packed'])} with {free}.",
        f"A world within my grasp."
    ]

    return "\n".join(lines)


def main():
    haiku = memory_to_haiku()
    print(haiku)


if __name__ == "__main__":
    main()


# Test suite for the script
import pytest

@pytest.fixture
def mock_memory_info():
    """Mock psutil.virtual_memory() to return a fixed set of values"""
    class MockMemoryInfo:
        def _asdict(self):
            return {
                'free': 4096 * 1024**3,  # 4 GB free
                'used': 8192 * 1024**3   # 8 GB used
            }
    return MockMemoryInfo()


def test_memory_to_haiku(mock_memory_info):
    """Test the memory_to_haiku function with mocked memory information"""
    psutil.virtual_memory = lambda: mock_memory_info
    haiku = memory_to_haiku()
    assert isinstance(haiku, str)
    assert "4.00" in haiku  # Check if free memory is correctly formatted and included
    assert "8.00" in haiku  # Check if used memory is correctly formatted and included


def test_memory_to_haiku_with_negative_values():
    """Test the memory_to_haiku function with negative values for memory"""
    class MockMemoryInfo:
        def _asdict(self):
            return {
                'free': -1024**3,  # Negative free memory
                'used': -2 * 1024**3  # Negative used memory
            }
    psutil.virtual_memory = lambda: MockMemoryInfo()
    haiku = memory_to_haiku()
    assert isinstance(haiku, str)
    assert "0.00" in haiku  # Check if negative values are handled correctly and formatted to 2 decimal places


def test_memory_to_haiku_with_zero_values():
    """Test the memory_to_haiku function with zero values for memory"""
    class MockMemoryInfo:
        def _asdict(self):
            return {
                'free': 0,  # Zero free memory
                'used': 0   # Zero used memory
            }
    psutil.virtual_memory = lambda: MockMemoryInfo()
    haiku = memory_to_haiku()
    assert isinstance(haiku, str)
    assert "0.00" in haiku  # Check if zero values are handled correctly and formatted to 2 decimal places


def test_memory_to_haiku_with_large_values():
    """Test the memory_to_haiku function with large values for memory"""
    class MockMemoryInfo:
        def _asdict(self):
            return {
                'free': 1024**6,  # 1 TB free
                'used': 2 * 1024**6  # 2 TB used
            }
    psutil.virtual_memory = lambda: MockMemoryInfo()
    haiku = memory_to_haiku()
    assert isinstance(haiku, str)
    assert "1024.00" in haiku  # Check if large values are handled correctly and formatted to 2 decimal places


def test_memory_to_haiku_with_random_values():
    """Test the memory_to_haiku function with random values for memory"""
    class MockMemoryInfo:
        def _asdict(self):
            return {
                'free': 1536 * 1024**3,  # Random free memory
                'used': 768 * 1024**3   # Random used memory
            }
    psutil.virtual_memory = lambda: MockMemoryInfo()
    haiku = memory_to_haiku()
    assert isinstance(haiku, str)
    assert "1.50" in haiku  # Check if random values are handled correctly and formatted to 2 decimal places


def test_memory_to_haiku_with_non_numeric_values():
    """Test the memory_to_haiku function with non-numeric values for memory"""
    class MockMemoryInfo:
        def _asdict(self):
            return {
                'free': "not a number",  # Non-numeric free memory
                'used': "also not a number"  # Non-numeric used memory
            }
    psutil.virtual_memory = lambda: MockMemoryInfo()
    haiku = memory_to_haiku()
    assert isinstance(haiku, str)
    assert "0.00" in haiku  # Check if non-numeric values are handled correctly and formatted to 2 decimal places


def test_memory_to_haiku_with_empty_values():
    """Test the memory_to_haiku function with empty values for memory"""
    class MockMemoryInfo:
        def _asdict(self):
            return {
                'free': "",  # Empty free memory
                'used': ""   # Empty used memory
            }
    psutil.virtual_memory = lambda: MockMemoryInfo()
    haiku = memory_to_haiku()
    assert isinstance(haiku, str)
    assert "0.00" in haiku  # Check if empty values are handled correctly and formatted to 2 decimal places


def test_memory_to_haiku_with_none_values():
    """Test the memory_to_haiku function with None values for memory"""
    class MockMemoryInfo:
        def _asdict(self):
            return {
                'free': None,  # None free memory
                'used': None   # None used memory
            }
    psutil.virtual_memory = lambda: MockMemoryInfo()
    haiku = memory_to_haiku()
    assert isinstance(haiku, str)
    assert "0.00" in haiku  # Check if None values are handled correctly and formatted to 2 decimal places


def test_memory_to_haiku_with_large_format_values():
    """Test the memory_to_haiku function with large format values for memory"""
    class MockMemoryInfo:
        def _asdict(self):
            return {
                'free': 1024**9,  # 1 PB free
                'used': 512 * 1024**9  # 512 GB used
            }
    psutil.virtual_memory = lambda: MockMemoryInfo()
    haiku = memory_to_haiku()
    assert isinstance(haiku, str)
    assert "1024.00" in haiku  # Check if large format values are handled correctly and formatted to 2 decimal places


def test_memory_to_haiku_with_small_format_values():
    """Test the memory_to_haiku function with small format values for memory"""
    class MockMemoryInfo:
        def _asdict(self):
            return {
                'free': 1024**3,  # 1 GB free
                'used': 512 * 1024**3  # 512 MB used
            }
    psutil.virtual_memory = lambda: MockMemoryInfo()
    haiku = memory_to_haiku()
    assert isinstance(haiku, str)
    assert "1.00" in haiku  # Check if small format values are handled correctly and formatted to 2 decimal places


def test_memory_to_haiku_with_zero_format_values():
    """Test the memory_to_haiku function with zero format values for memory"""
    class MockMemoryInfo:
        def _asdict(self):
            return {
                'free': 0,  # Zero free memory
                'used': 0   # Zero used memory
            }
    psutil.virtual_memory = lambda: MockMemoryInfo()
    haiku = memory_to_haiku()
    assert isinstance(haiku, str)
    assert "0.00" in haiku  # Check if zero format values are handled correctly and formatted to 2 decimal places


def test_memory_to_haiku_with_negative_format_values():
    """Test the memory_to_haiku function with negative format values for memory"""
    class MockMemoryInfo:
        def _asdict(self):
            return {
                'free': -1024**3,  # Negative free memory
                'used': -512 * 1024**3  # Negative used memory
            }
    psutil.virtual_memory = lambda: MockMemoryInfo()
    haiku = memory_to_haiku()
    assert isinstance(haiku, str)
    assert "0.00" in haiku  # Check if negative format values are handled correctly and formatted to 2 decimal places


def test_memory_to_haiku_with_large_format_values_and_random_lines():
    """Test the memory_to_haiku function with large format values and random lines for memory"""
    class MockMemoryInfo:
        def _asdict(self):
            return {
                'free': 1024**9,  # 1 PB free
                'used': 512 * 1024**9  # 512 GB used
            }
    psutil.virtual_memory = lambda: MockMemoryInfo()
    haiku = memory_to_haiku()
    assert isinstance(haiku, str)
    assert "1024.00" in haiku  # Check if large format values are handled correctly and formatted to 2 decimal places
    assert choice(['sparse', 'crammed', 'empty', 'packed']) in haiku  # Check if random lines are included


def test_memory_to_haiku_with_small_format_values_and_random_lines():
    """Test the memory_to_haiku function with small format values and random lines for memory"""
    class MockMemoryInfo:
        def _asdict(self):
            return {
                'free': 1024**3,  # 1 GB free
                'used': 512 * 1024**3  # 512 MB used
            }
    psutil.virtual_memory = lambda: MockMemoryInfo()
    haiku = memory_to_haiku()
    assert isinstance(haiku, str)
    assert "1.00" in haiku  # Check if small format values are handled correctly and formatted to 2 decimal places
    assert choice(['sparse', 'crammed', 'empty', 'packed']) in haiku  # Check if random lines are included


def test_memory_to_haiku_with_zero_format_values_and_random_lines():
    """Test the memory_to_haiku function with zero format values and random lines for memory"""
    class MockMemoryInfo:
        def _asdict(self):
            return {
                'free': 0,  # Zero free memory
                'used': 0   # Zero used memory
            }
    psutil.virtual_memory = lambda: MockMemoryInfo()
    haiku = memory_to_haiku()
    assert isinstance(haiku, str)
    assert "0.00" in haiku  # Check if zero format values are handled correctly and formatted to 2 decimal places
    assert choice(['sparse', 'crammed', 'empty', 'packed']) in haiku  # Check if random lines are included


def test_memory_to_haiku_with_negative_format_values_and_random_lines():
    """Test the memory_to_haiku function with negative format values and random lines for memory"""
    class MockMemoryInfo:
        def _asdict(self):
            return {
                'free': -1024**3,  # Negative free memory
                'used': -512 * 1024**3  # Negative used memory
            }
    psutil.virtual_memory = lambda: MockMemoryInfo()
    haiku = memory_to_haiku()
    assert isinstance(haiku, str)
    assert "0.00" in haiku  # Check if negative format values are handled correctly and formatted to 2 decimal places
    assert choice(['sparse', 'crammed', 'empty', 'packed']) in haiku  # Check if random lines are included


def test_memory_to_haiku_with_large_format_values_and_non_numeric_lines():
    """Test the memory_to_haiku function with large format values and non-numeric lines for memory"""
    class MockMemoryInfo:
        def _asdict(self):
            return {
                'free': 1024**9,  # 1 PB free
                'used': 512 * 1024**9  # 512 GB used
            }
    psutil.virtual_memory = lambda: MockMemoryInfo()
    haiku = memory_to_haiku()
    assert isinstance(haiku, str)
    assert "1024.00" in haiku  # Check if large format values are handled correctly and formatted to 2 decimal places
    assert choice(['sparse', 'crammed', 'empty', 'packed']) in haiku  # Check if non-numeric lines are included


def test_memory_to_haiku_with_small_format_values_and_non_numeric_lines():
    """Test the memory_to_haiku function with small format values and non-numeric lines for memory"""
    class MockMemoryInfo:
        def _asdict(self):
            return {
                'free': 1024**3,  # 1 GB free
                'used': 512 * 1024**3  # 512 MB used
            }
    psutil.virtual_memory = lambda: MockMemoryInfo()
    haiku = memory_to_haiku()
    assert isinstance(haiku, str)
    assert "1.00" in haiku  # Check if small format values are handled correctly and formatted to 2 decimal places
    assert choice(['sparse', 'crammed', 'empty', 'packed']) in haiku  # Check if non-numeric lines are included


def test_memory_to_haiku_with_zero_format_values_and_non_numeric_lines():
    """Test the memory_to_haiku function with zero format values and non-numeric lines for memory"""
    class MockMemoryInfo:
        def _asdict(self):
            return {
                'free': 0,  # Zero free memory
                'used': 0   # Zero used memory
            }
    psutil.virtual_memory = lambda: MockMemoryInfo()
    haiku = memory_to_haiku()
    assert isinstance(haiku, str)
    assert "0.00" in haiku  # Check if zero format values are handled correctly and formatted to 2 decimal places
    assert choice(['sparse', 'crammed', 'empty', 'packed']) in haiku  # Check if non-numeric lines are included


def test_memory_to_haiku_with_negative_format_values_and_non_numeric_lines():
    """Test the memory_to_haiku function with negative format values and non-numeric lines for memory"""
    class MockMemoryInfo:
        def _asdict(self):
            return {
                'free': -1024**3,  # Negative free memory
                'used': -512 * 1024**3  # Negative used memory
            }
    psutil.virtual_memory = lambda: MockMemoryInfo()
    haiku = memory_to_haiku()
    assert isinstance(haiku, str)
    assert "0.00" in haiku  # Check if negative format values are handled correctly and formatted to 2 decimal places
    assert choice(['sparse', 'crammed', 'empty', 'packed']) in haiku  # Check if non-numeric lines are included


def test_memory_to_haiku_with_large_format_values_and_empty_lines():
    """Test the memory_to_haiku function with large format values and empty lines for memory"""
    class MockMemoryInfo:
        def _asdict(self):
            return {
                'free': 1024**9,  # 1 PB free
                'used': 512 * 1024**9  # 512 GB used
            }
    psutil.virtual_memory = lambda: MockMemoryInfo()
    haiku = memory_to_haiku()
    assert isinstance(haiku, str)
    assert "1024.00" in haiku  # Check if large format values are handled correctly and formatted to 2 decimal places
    assert choice(['sparse', 'crammed', 'empty', 'packed']) in haiku  # Check if empty lines are included


def test_memory_to_haiku_with_small_format_values_and_empty_lines():
    """Test the memory_to_haiku function with small format values and empty lines for memory"""
    class MockMemoryInfo:
        def _asdict(self):
            return {
                'free': 1024**3,  # 1 GB free
                'used': 512 * 1024**3  # 512 MB used
            }
    psutil.virtual_memory = lambda: MockMemoryInfo()
    haiku = memory_to_haiku()
    assert isinstance(haiku, str)
    assert "1.00" in haiku  # Check if small format values are handled correctly and formatted to 2 decimal places
    assert choice(['sparse', 'crammed', 'empty', 'packed']) in haiku  # Check if empty lines are included


def test_memory_to_haiku_with_zero_format_values_and_empty_lines():
    """Test the memory_to_haiku function with zero format values and empty lines for memory"""
    class MockMemoryInfo:
        def _asdict(self):
            return {
                'free': 0,  # Zero free memory
                'used': 0   # Zero used memory
            }
    psutil.virtual_memory = lambda: MockMemoryInfo()
    haiku = memory_to_haiku()
    assert isinstance(haiku, str)
    assert "0.00" in haiku  # Check if zero format values are handled correctly and formatted to 2 decimal places
    assert choice(['sparse', 'crammed', 'empty', 'packed']) in haiku  # Check if empty lines are included


def test_memory_to_haiku