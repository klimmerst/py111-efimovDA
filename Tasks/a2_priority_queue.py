"""
Priority Queue

Queue priorities are from 0 to 10
"""
from typing import Any

pqueue = {}


def enqueue(elem: Any, priority: int = 0) -> None:
    """
    Operation that add element to the end of the queue

    :param elem: element to be added
    :return: Nothing
    """
    if priority in pqueue:
        pqueue[priority].append(elem)
    else:
        pqueue[priority] = [elem]

    return None


def dequeue() -> Any:
    """
    Return element from the beginning of the queue. Should return None if not elements.

    :return: dequeued element
    """
    if len(pqueue):
        m = min(pqueue.keys())
        value = pqueue[m].pop(0)
        if not pqueue[m]:
            pqueue.pop(m)
        return value

    return None


def peek(ind: int = 0, priority: int = 0) -> Any:
    """
    Allow you to see at the element in the queue without dequeuing it

    :param ind: index of element (count from the beginning)
    :return: peeked element
    """
    if priority in pqueue and 0 <= ind < len(pqueue[priority]):
        return pqueue[priority][ind]

    return None


def clear() -> None:
    """
    Clear my queue

    :return: None
    """
    pqueue.clear()

    return None
