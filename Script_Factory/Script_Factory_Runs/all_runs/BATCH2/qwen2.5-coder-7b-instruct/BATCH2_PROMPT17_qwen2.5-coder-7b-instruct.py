import time

class AnticipatoryCachingSystem:
    def __init__(self):
        self.cache = {}
        self.data_source = self.generate_data()  # Simulated data source

    def generate_data(self):
        # This is a simple generator that yields numbers
        i = 0
        while True:
            yield i
            i += 1

    def get_item(self, key):
        if key not in self.cache:
            start_time = time.time()
            for i in range(key, key + 6):  # Preemptively fetch next five items
                self.cache[i] = next(self.data_source)
            print(f"Time taken to cache {key} and next five items: {time.time() - start_time:.2f} seconds")
        return self.cache[key]

if __name__ == "__main__":
    caching_system = AnticipatoryCachingSystem()
    # Example usage
    for i in range(10):
        print(f"Retrieving item {i}: {caching_system.get_item(i)}")
```

This Python program implements an anticipatory caching system where, when a user requests a piece of data, it returns the requested data but also preemptively fetches the next five items in the list and stores them in memory. The `get_item` method checks if the item is already in the cache; if not, it fetches the item and the next five items from the simulated data source and stores them in the cache. The `if __name__ == "__main__":` block demonstrates how to use the caching system by retrieving items.