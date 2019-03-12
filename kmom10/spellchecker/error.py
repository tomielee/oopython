#! usr/local/bin/env python3
"""
    Custom exceptions
    Kmom010
"""

class Error(Exception):
    """basklass som ärver från inbyggda Exception"""
    pass

class NoFile(Error):
    """raised error when unable to open file"""
    pass

class EmptyTree(Error):
    """raised error when first node and empty tree"""
    pass

class NoRead(Error):
    """raised error when unable to read file"""
    pass

class NoContent(Error):
    """raised error when unable to get content from file"""
    pass

class SearchError(Error):
    """reaise error when no unable to match searchresult"""
    pass

class SomethingWrong(Error):
    """raised error when unable to continue"""
    pass
