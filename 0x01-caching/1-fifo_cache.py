#!/usr/bin/env python3

'''class FIFOCache that inherits from BaseCaching and is a caching system'''
from collections import OrderedDict
from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """ FIFO caching system """

    def __init__(self):
        """ Initialize FIFO caching system """
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """ Add an item in the cache """
        self.cache_data[key] = item

        if key is None or item is None:
            return

        if len(self.cache_data) > self.MAX_ITEMS:
            first = next(iter(self.cache_data))
            self.cache_data.pop(first)
            print("DISCARD: {}".format(first))
        self.cache_data.move_to_end(key)

    def get(self, key):
        """ Get an item by key """
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data.get(key, None)
