from typing import Sequence, Optional


def binary_search(elem: int, arr: Sequence) -> Optional[int]:
    """
    Performs binary search of given element inside of array (using recursive way)

    :param elem: element to be found
    :param arr: array where element is to be found
    :return: Index of element if it's presented in the arr, None otherwise
    """
    if not arr:
        return None

    left = 0
    right = len(arr) - 1

    mid = (left + right) // 2

    if arr[mid] == elem:
        while mid >= 1 and arr[mid - 1] == elem:
            mid -= 1
        return mid

    if elem > arr[mid]:
        left = mid + 1
        arr = arr[left:]
        buf = binary_search(elem, arr)
        if buf is not None:
            return buf + mid + 1

    elif elem < arr[mid]:
        right = mid
        arr = arr[:right]
        buf = binary_search(elem, arr)
        if buf is not None:
            return buf

    return None
