# BATCH3_PROMPT17_Devstral.py

import time
from collections import OrderedDict

class LRUCache:
    """Least Recently Used Cache implementation with anticipatory fetching."""
    
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = OrderedDict()
    
    def get(self, key: str):
        """Get an item from the cache and mark it as recently used."""
        if key in self.cache:
            # Move the accessed item to the end to mark it as recently used
            self.cache.move_to_end(key)
            return self.cache[key]
        return None
    
    def put(self, key: str, value):
        """Add an item to the cache."""
        if key in self.cache:
            # Move existing item to end (mark as recently used)
            self.cache.move_to_end(key)
        self.cache[key] = value
        if len(self.cache) > self.capacity:
            # Pop the first item (least recently used)
            self.cache.popitem(last=False)

class AnticipatoryCache(LRUCache):
    """Anticipatory Cache that pre-fetches next 5 items."""
    
    def __init__(self, capacity: int, data_source):
        super().__init__(capacity)
        self.data_source = data_source
        # Pre-fetch initial items if the source is a list and not empty
        self._prefetch_initial_items()
    
    def _prefetch_initial_items(self):
        """Prefetch initial cache with first N items from data source."""
        if isinstance(self.data_source, (list, tuple)) and len(self.data_source) > 0:
            for i in range(min(5, len(self.data_source))):
                self.put(str(i), self.data_source[i])
    
    def get(self, key: str):
        """Get item from cache with anticipatory fetching."""
        result = super().get(key)
        if result is not None:
            # Try to prefetch next 5 items if they exist in data source
            try:
                key_index = int(key)
                for i in range(1, 6):  # Prefetch next 5 items
                    next_key = str(key_index + i)
                    if next_key not in self.cache and key_index + i < len(self.data_source):
                        self.put(next_key, self.data_source[key_index + i])
            except ValueError:
                pass  # Key is not an integer, skip prefetching
        return result

def main():
    """Demonstrate the anticipatory cache functionality."""
    
    # Sample data source (could be any iterable)
    data = [f"Item {i}" for i in range(20)]

    print("Initializing Anticipatory Cache with capacity 10 and sample data...")
    cache = AnticipatoryCache(capacity=10, data_source=data)

    # Simulate some cache accesses
    access_pattern = [0, 1, 5, 3, 8, 2, 6]

    print("\nAccess pattern:", access_pattern)
    print("Cache contents after each access:")
    
    for key in access_pattern:
        print(f"\nAccessing item {key}:")
        value = cache.get(str(key))
        if value:
            print(f"Retrieved: {value}")
        else:
            print("Item not found")

        # Display current cache state (first 10 items)
        print("Current cache state:")
        for k, v in list(cache.cache.items())[:10]:
            print(f"  {k}: {v}")

if __name__ == "__main__":
    main()