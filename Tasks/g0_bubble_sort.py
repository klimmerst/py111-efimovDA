from typing import List


def sort(container: List[int]) -> List[int]:
    """
    Sort input container with bubble sort

    :param container: container of elements to be sorted
    :return: container sorted in ascending order
    """

    for i in range(len(container) - 1):
        for j in range(len(container) - i - 1):
            print(container)
            if container[j] > container[j + 1]:
                container[j], container[j + 1] = container[j + 1], container[j]

    return container
