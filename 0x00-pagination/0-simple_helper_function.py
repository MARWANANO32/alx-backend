#!/usr/bin/env python3
"""function named index_range that takes two integer arguments.
"""
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """The function should return a tuple of size
    two containing a start index and an end index corresponding
      to the range of indexes to return in a list for those particular
        pagination parameters."""

    first_index = (page - 1) * page_size
    second_index = page * page_size
    return (first_index, second_index)
