"""
You can do it either with networkx ('cause tree is a graph)
or with dicts (smth like {'key': 0, value: 123, 'left': {...}, 'right':{...}})
"""

from typing import Any, Optional, Tuple
# import networkx as nx

dict = {}

def insert(key: int, value: Any) -> None:
    """
    Insert (key, value) pair to binary search tree

    :param key: key from pair (key is used for positioning node in the tree)
    :param value: value associated with key
    :return: None
    """

    buf = dict

    if not dict:
        buf['key'] = key
        buf['value'] = value
        buf['left'] = {}
        buf['right'] = {}
        return None

    while True:
        if key == buf['key']:
            return None
        elif key < buf['key']:
            buf = buf['left']
        elif key > buf['key']:
            buf = buf['right']
        if not buf:
            buf['key'] = key
            buf['value'] = value
            buf['left'] = {}
            buf['right'] = {}
            return None

def remove(key: int) -> Optional[Tuple[int, Any]]:
    """
    Remove key and associated value from the BST if exists

    :param key: key to be removed
    :return: deleted (key, value) pair or None
    """

    if not dict:
        return None

    buf = dict
    buf_2 = buf

    while buf:
        if buf['key'] == key:
            buf_2 = {}
            return buf['value']
        elif key < buf['key']:
            buf_2 = buf
            buf = buf['left']
        elif key > buf['key']:
            buf_2 = buf
            buf = buf['right']

def find(key: int) -> Optional[Any]:
    """
    Find value by given key in the BST

    :param key: key for search in the BST
    :return: value associated with the corresponding key
    """

    if not dict:
        raise KeyError

    buf = dict

    while buf:
        if buf['key'] == key:
            return buf['value']
        elif key < buf['key']:
            buf = buf['left']
        elif key > buf['key']:
            buf = buf['right']

    raise KeyError


def clear() -> None:
    """
    Clear the tree

    :return: None
    """

    dict.clear()

    return None