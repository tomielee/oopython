#! usr/local/bin/env python3
"""
    Custom exceptions
    Kmom04
"""

class Error(Exception):
    """basklass som ärver från inbyggda Exception"""
    pass


class OutOfIndex(Error):
    """raised error when out of index"""
    pass

class AttError(Error):
    """raised error when out of index"""
    pass

class TypeErr(Error):
    """raides error when wrong type"""
    pass

class WrongType(Error):
    """raides error when wrong type"""
    pass

class NoValue(Error):
    """can't find value"""
    pass
