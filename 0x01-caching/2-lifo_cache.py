#!/usr/bin/env python3

'''class LIFOCache that inherits from BaseCaching and is a caching system'''
from collections import OrderedDict
from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """ LIFO caching system """

    def __init__(self):
        """ Initialize LIFO caching system """
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """ Add an item in the cache """

        if key is None or item is None:
            return
        self.cache_data[key] = item

        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            last_key = list(self.cache_data.keys())[-2]
            print(f"DISCARD: {last_key}")
            self.cache_data.popitem(last=True)

    def get(self, key):
        """ Get an item by key """
        if key is None or key not in self.cache_data:
            return None

        return self.cache_data.get(key, None)
