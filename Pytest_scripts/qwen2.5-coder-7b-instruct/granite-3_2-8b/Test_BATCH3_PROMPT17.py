# BATCH3_PROMPT17_Granite.py

class AnticipatoryCache:
    def __init__(self):
        self.data = []  # List to store cached data
        self.fetched_items = set()  # Set to track fetched items to avoid duplicates

    def fetch_and_cache(self, data_list):
        """Fetch and cache next five items in the list."""
        if not data_list:
            return

        for i in range(min(5, len(data_list))):
            item = data_list[i]

            # Skip already fetched items
            if item in self.fetched_items:
                continue

            self.fetched_items.add(item)
            print(f"Fetching {item}...")
            # Simulate network delay with time.sleep
            import time
            time.sleep(1)  # Replace this with actual fetching logic
            self.data.append(item)

    def get_data(self, index):
        """Return data at the given index from cache."""
        return self.data[index] if 0 <= index < len(self.data) else None

def main():
    cache = AnticipatoryCache()
    data_list = ['item1', 'item2', 'item3', 'item4', 'item5', 'item6', 'item7']

    # Simulate initial requests and anticipatory caching
    for i in range(0, len(data_list), 2):
        cache.fetch_and_cache(data_list)
        print(f"Requesting data at index {i}: ", end='')
        requested_data = cache.get_data(i)
        if requested_data:
            print(requested_data)
        else:
            print("Not found in cache")

    # Additional requests to demonstrate the effect of caching
    for _ in range(5):
        index = len(cache.data) // 2  # Randomly choose an index from cached data
        print(f"Requesting random data at index {index}: ", end='')
        requested_data = cache.get_data(index)
        if requested_data:
            print(requested_data)
        else:
            print("Not found in cache")

if __name__ == "__main__":
    main()

# ===== GENERATED TESTS =====
```python
# BATCH3_PROMPT17_Granite.py

class AnticipatoryCache:
    def __init__(self):
        self.data = []  # List to store cached data
        self.fetched_items = set()  # Set to track fetched items to avoid duplicates

    def fetch_and_cache(self, data_list):
        """Fetch and cache next five items in the list."""
        if not data_list:
            return

        for i in range(min(5, len(data_list))):
            item = data_list[i]

            # Skip already fetched items
            if item in self.fetched_items:
                continue

            self.fetched_items.add(item)
            print(f"Fetching {item}...")
            # Simulate network delay with time.sleep
            import time
            time.sleep(1)  # Replace this with actual fetching logic
            self.data.append(item)

    def get_data(self, index):
        """Return data at the given index from cache."""
        return self.data[index] if 0 <= index < len(self.data) else None

def main():
    cache = AnticipatoryCache()
    data_list = ['item1', 'item2', 'item3', 'item4', 'item5', 'item6', 'item7']

    # Simulate initial requests and anticipatory caching
    for i in range(0, len(data_list), 2):
        cache.fetch_and_cache(data_list)
        print(f"Requesting data at index {i}: ", end='')
        requested_data = cache.get_data(i)
        if requested_data:
            print(requested_data)
        else:
            print("Not found in cache")

    # Additional requests to demonstrate the effect of caching
    for _ in range(5):
        index = len(cache.data) // 2  # Randomly choose an index from cached data
        print(f"Requesting random data at index {index}: ", end='')
        requested_data = cache.get_data(index)
        if requested_data:
            print(requested_data)
        else:
            print("Not found in cache")

if __name__ == "__main__":
    main()

# Test suite for BATCH3_PROMPT17_Granite.py

import pytest
from typing import List, Optional
from unittest.mock import patch

@pytest.fixture
def cache():
    return AnticipatoryCache()

@pytest.mark.parametrize("data_list, expected_fetched_items", [
    (['item1', 'item2'], {'item1', 'item2'}),
    (['item3', 'item4', 'item5'], {'item3', 'item4', 'item5'}),
    ([], set()),
])
def test_fetch_and_cache(cache: AnticipatoryCache, data_list: List[str], expected_fetched_items: set):
    """Test the fetch_and_cache method."""
    cache.fetch_and_cache(data_list)
    assert cache.fetched_items == expected_fetched_items

@pytest.mark.parametrize("index, expected_data", [
    (0, 'item1'),
    (2, 'item3'),
    (5, None),
])
def test_get_data(cache: AnticipatoryCache, index: int, expected_data: Optional[str]):
    """Test the get_data method."""
    cache.data = ['item1', 'item2', 'item3']
    assert cache.get_data(index) == expected_data

@patch('time.sleep')
def test_fetch_and_cache_with_sleep(mock_sleep):
    """Test the fetch_and_cache method with time.sleep patched."""
    cache = AnticipatoryCache()
    data_list = ['item1', 'item2', 'item3', 'item4', 'item5']
    cache.fetch_and_cache(data_list)
    mock_sleep.assert_called_once()

@patch('time.sleep')
def test_fetch_and_cache_with_empty_list(mock_sleep):
    """Test the fetch_and_cache method with an empty list."""
    cache = AnticipatoryCache()
    data_list = []
    cache.fetch_and_cache(data_list)
    mock_sleep.assert_not_called()

@patch('time.sleep')
def test_get_data_with_index_out_of_range(mock_sleep):
    """Test the get_data method with an index out of range."""
    cache = AnticipatoryCache()
    data_list = ['item1', 'item2']
    cache.fetch_and_cache(data_list)
    assert cache.get_data(5) is None
```