#!/usr/bin/env python3
""" LRU Caching """
from base_caching import BaseCaching
from typing import Dict, Optional, Any


class LRUCache(BaseCaching):
    """ LRU caching class """

    def __init__(self):
        """LRU Constructor """
        super().__init__()
        self.queue = []

    def put(self, key: Any, item: Any) -> None:
        """ Caches data in LRUCache """
        if key is None or item is None:
            return

        self.cache_data[key] = item

        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            first = self.queue[0] if self.queue else None
            if first:
                self.queue.pop(0)
                del self.cache_data[first]
                print("DISCARD: {}".format(first))

        if key not in self.queue:
            self.queue.append(key)
        else:
            self.refactor_queue(key)

    def get(self, key: Any) -> Optional[Dict]:
        """ Retrieves item from cache """
        item = self.cache_data.get(key)
        if item is not None:
            self.refactor_queue(key)
        return item

    def refactor_queue(self, key: Any) -> None:
        """ Moves element to last index of list """
        if self.queue[-1] != key:
            self.queue.remove(key)
            self.queue.append(key)


if __name__ == "__main__":
    my_cache = LRUCache()
    my_cache.put("A", "Hello")
    my_cache.put("B", "World")
    my_cache.put("C", "Holberton")
    my_cache.put("D", "School")
    my_cache.print_cache()
    print(my_cache.get("B"))
    my_cache.put("E", "Battery")
    my_cache.print_cache()
    my_cache.put("C", "Street")
    my_cache.print_cache()
    print(my_cache.get("A"))
    print(my_cache.get("B"))
    print(my_cache.get("C"))
    my_cache.put("F", "Mission")
    my_cache.print_cache()
    my_cache.put("G", "San Francisco")
    my_cache.print_cache()
    my_cache.put("H", "H")
    my_cache.print_cache()
    my_cache.put("I", "I")
    my_cache.print_cache()
    my_cache.put("J", "J")
    my_cache.print_cache()
    my_cache.put("K", "K")
    my_cache.print_cache()
