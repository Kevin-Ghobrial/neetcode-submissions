class LRUCache:

    #idea: list value stores key, use that key for map
    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = OrderedDict() # remembers the order in which the values were added

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        self.cache.move_to_end(key)
        return self.cache[key]

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.cache.move_to_end(key)
        self.cache[key] = value

        if len(self.cache) > self.cap:
            self.cache.popitem(last=False) # first in first out

