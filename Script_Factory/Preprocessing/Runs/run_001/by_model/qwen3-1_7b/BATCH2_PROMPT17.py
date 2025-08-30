```python
import sys

class AnticipatoryCache:
    def __init__(self, data_list):
        self.cache = {}
        self.data_list = data_list
        
    def get(self, item):
        if item in self.cache:
            return item
        else:
            index = self.data_list.index(item)
            start = index + 1
            end = min(start + 5, len(self.data_list))
            fetched_items = self.data_list[start:end]
            for item_in_fetched in fetched_items:
                if item_in_fetched not in self.cache:
                    self.cache[item_in_fetched] = True
            self.cache[item] = True
            return item

if __name__ == "__main__":
    data_list = ['A', 'B', 'C', 'D', 'E']
    cache = AnticipatoryCache(data_list)
    print("Requesting A:", cache.get('A'))
    print("Requesting B:", cache.get('B'))
    print("Requesting C:", cache.get('C'))
    print("Requesting D:", cache.get('D'))
    print("Requesting E:", cache.get('E'))
    print("Requesting F:", cache.get('F'))