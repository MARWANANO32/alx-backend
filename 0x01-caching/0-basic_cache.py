#!/usr/bin/env python3
'''class BasicCache that inherits from BaseCaching and is a caching system'''

from base_caching import BaseCaching


class BasicCache(BaseCaching):
    '''basic caching system'''
    def put(self, key, item):
        '''method that puts items in cache
        if cache_data is full, one item is removed
        '''
        if key is not None and item is not None:
            self.cache_data[key] = item

    def get(self, key):
        '''method that gets items from cache
        if key is None or the key doesn't exist, return None
        '''
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data[key]
