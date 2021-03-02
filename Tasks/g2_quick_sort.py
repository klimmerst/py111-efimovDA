from typing import List
import random


def sort(container: List[int], left=None, right=None) -> List[int]:
    """
    Sort input container with quick sort

    :param container: container of elements to be sorted
    :return: container sorted in ascending order
    """

    if left is None:
        left = 0
        right = len(container) - 1

    if left < right:
        r = random.randint(left, right - 1)

        mid_n = (left + right) // 2

        mid = container[mid_n]

        container[r], container[mid_n] = container[mid_n], container[r]

        i = left - 1
        j = right + 1

        while True:
            i += 1
            while container[i] < mid:
                i += 1
            j -= 1
            while container[j] > mid:
                j -= 1
            if i >= j:
                break

            container[i], container[j] = container[j], container[i]

        sort(container, left, j)
        sort(container, j + 1, right)

    return container