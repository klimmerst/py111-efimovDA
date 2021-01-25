from typing import List


def sort(container: List[int]) -> List[int]:
    """
    Sort input container with quick sort

    :param container: container of elements to be sorted
    :return: container sorted in ascending order
    """

    if not container:
        return container
    
    if len(container) == 1:
        return container

    middle = len(container) // 2

    left_cont = []
    right_cont = []
    same_cont = []

    for i in container:
        if i > container[middle]:
            right_cont.append(i)
        elif i < container[middle]:
            left_cont.append(i)
        elif i == container[middle]:
            same_cont.append(i)

    return sort(left_cont) + same_cont + sort(right_cont)
