from typing import List


def sort(container: List[int]) -> List[int]:
    """
    Sort input container with merge sort

    :param container: container of elements to be sorted
    :return: container sorted in ascending order
    """

    if len(container) == 1:
        return container

    middle = len(container) // 2
    left = sort(container[:middle])
    right = sort(container[middle:])

    count_l = 0
    count_r = 0
    final_list = []

    while count_r < len(left) and count_l < len(right):

        if right[count_l] <= left[count_r]:
            final_list.append(right[count_l])
            count_l += 1
        else:
            final_list.append(left[count_r])
            count_r += 1
        if count_r == len(left):
            final_list += right[count_l:]
        if count_l == len(right):
            final_list += left[count_r:]

    return final_list
