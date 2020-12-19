"""
My little Stack
"""
from typing import Any

my_stack = []  # вершина справа

def push(elem: Any) -> None:
    """
    Operation that add element to stack

    :param elem: element to be pushed
    :return: Nothing
    """
    print(elem)  # в данном слукчае принт нам не нужен, можем его удалять

    my_stack.append(elem)  # добавляем элемент в конце списка
    return None


def pop() -> Any:
    """
    Pop element from the top of the stack. If not elements - should return None.

    :return: popped element
    """
    return None


def peek(ind: int = 0) -> Any:
    """
    Allow you to see at the element in the stack without popping it.

    :param ind: index of element (count from the top, 0 - top, 1 - first from top, etc.)
    :return: peeked element or None if no element in this place
    """
    print(ind)
    return None


def clear() -> None:
    """
    Clear my stack

    :return: None
    """

    my_stack.clear()
    return None


if __name__ == '__main__':  # не совсем понятно
    print(my_stack)
    push(1)
    print(my_stack)
    push(2)
    print(my_stack)


    clear()
    print(my_stack)