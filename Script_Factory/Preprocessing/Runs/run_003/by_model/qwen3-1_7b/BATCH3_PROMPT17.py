```python
import sys

def get_item(item):
    """Fetches data from the cache and preempts fetching next five items if needed."""
    if item in cache:
        return item
    # Fetch the next five items from the predefined list starting at current index
    for i in range(current_index, min(current_index + 5, len(data_list))):
        if i < len(data_list):
            cache.add(data_list[i])
            current_index = i + 1
    return item

if __name__ == "__main__":
    """Main entry point for the Anticipatory Caching System simulation."""
    data_list = ['A', 'B', 'C', 'D', 'E']
    cache = set()
    current_index = 0
    
    print("Anticipatory Caching System Simulation:")
    
    # Simulate user requests
    for i in range(5):
        item = data_list[i]
        result = get_item(item)
        print(f"Request: {item} -> Result: {result}")