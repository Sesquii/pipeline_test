# BATCH3_PROMPT17_{{model_name}}.py

import time

class AnticipatoryCache:
    def __init__(self, data_source):
        self.data_source = data_source
        self.cache = {}

    def fetch_data(self, key):
        if key not in self.cache:
            self.cache[key] = self.data_source.get(key)
        return self.cache[key]

    def get_next_items(self, current_key):
        next_keys = [current_key + i for i in range(1, 6)]
        for key in next_keys:
            self.fetch_data(key)

def data_source(key):
    # Simulate a time-consuming data fetch
    time.sleep(0.5)
    return f"Data for {key}"

if __name__ == "__main__":
    cache = AnticipatoryCache(data_source)
    
    # Simulate user requests
    requested_key = 'item1'
    print(f"Requesting: {requested_key}")
    result = cache.fetch_data(requested_key)
    print(result)
    
    # Preemptively fetch next items
    cache.get_next_items(requested_key)

# ===== GENERATED TESTS =====
# BATCH3_PROMPT17_{{model_name}}.py

import time
from typing import Any, Callable, Dict

class AnticipatoryCache:
    def __init__(self, data_source: Callable[[str], str]):
        self.data_source = data_source
        self.cache: Dict[str, str] = {}

    def fetch_data(self, key: str) -> str:
        if key not in self.cache:
            self.cache[key] = self.data_source(key)
        return self.cache[key]

    def get_next_items(self, current_key: str) -> None:
        next_keys = [current_key + str(i) for i in range(1, 6)]
        for key in next_keys:
            self.fetch_data(key)

def data_source(key: str) -> str:
    # Simulate a time-consuming data fetch
    time.sleep(0.5)
    return f"Data for {key}"

if __name__ == "__main__":
    cache = AnticipatoryCache(data_source)
    
    # Simulate user requests
    requested_key = 'item1'
    print(f"Requesting: {requested_key}")
    result = cache.fetch_data(requested_key)
    print(result)
    
    # Preemptively fetch next items
    cache.get_next_items(requested_key)

# Test suite for AnticipatoryCache class

import pytest

@pytest.fixture
def mock_data_source():
    def mock_function(key):
        return f"Mock Data for {key}"
    return mock_function

def test_fetch_data(mock_data_source):
    """Test the fetch_data method with a mock data source."""
    cache = AnticipatoryCache(mock_data_source)
    key = 'item1'
    result = cache.fetch_data(key)
    assert result == "Mock Data for item1"
    assert key in cache.cache

def test_get_next_items(mock_data_source):
    """Test the get_next_items method with a mock data source."""
    cache = AnticipatoryCache(mock_data_source)
    current_key = 'item1'
    cache.get_next_items(current_key)
    expected_keys = [current_key + str(i) for i in range(1, 6)]
    for key in expected_keys:
        assert key in cache.cache

def test_fetch_data_cache_hit(mock_data_source):
    """Test the fetch_data method when data is already cached."""
    cache = AnticipatoryCache(mock_data_source)
    key = 'item1'
    cache.fetch_data(key)  # First fetch to populate cache
    result = cache.fetch_data(key)  # Second fetch from cache
    assert result == "Mock Data for item1"
    assert len(cache.cache) == 1

def test_get_next_items_cache_hit(mock_data_source):
    """Test the get_next_items method when data is already cached."""
    cache = AnticipatoryCache(mock_data_source)
    current_key = 'item1'
    cache.get_next_items(current_key)  # First fetch to populate cache
    cache.get_next_items(current_key)  # Second fetch from cache
    expected_keys = [current_key + str(i) for i in range(1, 6)]
    for key in expected_keys:
        assert len(cache.cache) == 5

def test_fetch_data_with_nonexistent_key(mock_data_source):
    """Test the fetch_data method with a nonexistent key."""
    cache = AnticipatoryCache(mock_data_source)
    key = 'nonexistent'
    result = cache.fetch_data(key)
    assert result == "Mock Data for nonexistent"
    assert key in cache.cache

def test_get_next_items_with_nonexistent_key(mock_data_source):
    """Test the get_next_items method with a nonexistent key."""
    cache = AnticipatoryCache(mock_data_source)
    current_key = 'nonexistent'
    cache.get_next_items(current_key)
    expected_keys = [current_key + str(i) for i in range(1, 6)]
    for key in expected_keys:
        assert key in cache.cache

def test_fetch_data_with_empty_key(mock_data_source):
    """Test the fetch_data method with an empty key."""
    cache = AnticipatoryCache(mock_data_source)
    key = ''
    result = cache.fetch_data(key)
    assert result == "Mock Data for "
    assert key in cache.cache

def test_get_next_items_with_empty_key(mock_data_source):
    """Test the get_next_items method with an empty key."""
    cache = AnticipatoryCache(mock_data_source)
    current_key = ''
    cache.get_next_items(current_key)
    expected_keys = [current_key + str(i) for i in range(1, 6)]
    for key in expected_keys:
        assert key in cache.cache

def test_fetch_data_with_large_number_of_requests(mock_data_source):
    """Test the fetch_data method with a large number of requests."""
    cache = AnticipatoryCache(mock_data_source)
    keys = [f'item{i}' for i in range(100)]
    for key in keys:
        result = cache.fetch_data(key)
        assert result == f"Mock Data for {key}"
        assert key in cache.cache

def test_get_next_items_with_large_number_of_requests(mock_data_source):
    """Test the get_next_items method with a large number of requests."""
    cache = AnticipatoryCache(mock_data_source)
    current_keys = [f'item{i}' for i in range(100)]
    for key in current_keys:
        cache.get_next_items(key)
        expected_keys = [key + str(i) for i in range(1, 6)]
        for sub_key in expected_keys:
            assert sub_key in cache.cache
