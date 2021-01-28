"""
This module implements some functions based on linear search algo
"""
from typing import Sequence


def min_search(arr: Sequence) -> int:

    if not arr:
        return -1

    minim = arr[0]
    index = 0

    for i in range(len(arr)):
        if arr[i] < minim:
            minim = arr[i]
            index = i

    return index