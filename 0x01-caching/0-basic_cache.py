#!/usr/bin/env python3
'''class BasicCache that inherits from BaseCaching and is a caching system'''

from base_caching import BaseCaching


class BasicCache(BaseCaching):
    '''basic caching system'''
    def put(self, key, item):
        '''method that puts items in cache'''
        if key is not None and item is not None:
            self.cache_data[key] = item

    def get(self, key):
        '''method that gets items from cache'''

        return self.cache_data[key]
