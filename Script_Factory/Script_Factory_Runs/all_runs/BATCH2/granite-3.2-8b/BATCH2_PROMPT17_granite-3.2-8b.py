# BATCH2_PROMPT17_Granite.py

class AnticipatoryCachingSystem:
    def __init__(self):
        self.cache = []

    def fetch(self, item):
        if item not in self.cache:
            self._fetch_item(item)
            return self._get_cached_item(item)
        else:
            return self._get_cached_item(item)

    def _fetch_item(self, item):
        # Simulate fetching an item from a data source (like a database or web API)
        print(f"Fetching {item}...")
        import time
        time.sleep(1)  # Simulate network latency
        self.cache.append(item)

    def _get_cached_item(self, item):
        index = self.cache.index(item)
        if index + 5 < len(self.cache):
            # Fetch the next five items anticipatorily
            for i in range(index + 1, min(index + 6, len(self.cache))):
                print(f"Anticipating fetch of {self.cache[i]}...")
                time.sleep(0.5)  # Simulate network latency
            return self.cache[index]
        else:
            return self.cache[index]


def main():
    cache_system = AnticipatoryCachingSystem()

    # Simulated user requests
    items_to_request = ['item1', 'item2', 'item3', 'item4', 'item5', 'item6']

    for item in items_to_request:
        result = cache_system.fetch(item)
        print(f"Returned: {result}")


if __name__ == "__main__":
    main()