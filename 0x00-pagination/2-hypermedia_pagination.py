#!/usr/bin/env python3
"""Pagination module
"""

import csv
import math
from typing import List


def index_range(page, page_size):
    """Give start and end index of pagination
    """
    return (page_size * (page - 1), page_size * page)


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """Page reader
        """
        assert type(page) == int
        assert page > 0
        assert type(page_size) == int
        assert page_size > 1

        start_idx, end_idx = index_range(page, page_size)
        if start_idx >= len(self.dataset()):
            return []

        return self.dataset()[start_idx: end_idx]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> List[List]:
        """hyper pagination loader
        """
        data = self.get_page(page, page_size)
        total_pages = math.ceil(len(self.dataset()) / page_size)
        if len(data) == 0:
            return {
                'page_size': 0,
                'page': page,
                'data': data,
                'next_page': None,
                'prev_page': page - 1 or None,
                'total_pages': total_pages
                }

        return {
             'page_size': page_size,
             'page': page,
             'data': data,
             'next_page': page + 1,
             'prev_page': page - 1 or None,
             'total_pages': total_pages
             }
