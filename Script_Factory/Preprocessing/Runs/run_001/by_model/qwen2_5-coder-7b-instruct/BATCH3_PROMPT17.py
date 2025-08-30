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