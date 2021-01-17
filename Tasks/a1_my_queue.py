"""
My little Queue
"""
from typing import Any

my_list = []


def enqueue(elem: Any) -> None:
    """
    Operation that add element to the end of the queue

    :param elem: element to be added
    :return: Nothing
    """

    my_list.append(elem)

    return None


def dequeue() -> Any:
    """
    Return element from the beginning of the queue. Should return None if no elements.

    :return: dequeued element
    """

    if not my_list:
        return None

    return my_list.pop(0)


def peek(ind: int = 0) -> Any:
    """
    Allow you to see at the element in the queue without dequeuing it

    :param ind: index of element (count from the beginning)
    :return: peeked element
    """

    if 0 <= ind <= len(my_list) - 1:
        return my_list[ind]
    else:
        return None


def clear() -> None:
    """
    Clear my queue

    :return: None
    """

    my_list.clear()

    return None
