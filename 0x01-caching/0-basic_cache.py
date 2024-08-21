#!/usr/bin/python3
'''class BasicCache that inherits from BaseCaching and is a caching system'''

from base_caching import BaseCaching


class BasicCache(BaseCaching):
    '''basic caching system'''
    def put(self, key, item):
        self.cache_data[key] = item
        '''method that puts items in cache'''
        if key and item is None:
            return

    def get(self, key):
        self.cache_data.get(key)
        '''method that gets items from cache'''
        if key is None:
            return None
