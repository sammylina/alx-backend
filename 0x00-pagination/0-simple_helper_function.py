#!/usr/bin/env python3
""" simple helper module
"""


def index_range(page, page_size):
    """return start and end index of pagination
    """
    return (page_size * (page - 1), page_size * page)
