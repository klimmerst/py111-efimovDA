def fib_recursive(n: int) -> int:
    """
    Calculate n-th number of Fibonacci sequence using recursive algorithm

    :param n: number of item
    :return: Fibonacci number
    """

    if n <= 0:
        raise ValueError

    if n in (1, 2):
        return 1

    return fib_recursive(n-1) + fib_recursive(n-2)


def fib_iterative(n: int) -> int:
    """
    Calculate n-th number of Fibonacci sequence using iterative algorithm

    :param n: number of item
    :return: Fibonacci number
    """

    if n <= 0:
        raise ValueError

    fib1 = 1
    fib2 = 1

    for i in range(n-2):
        fib1, fib2 = fib2, fib1 + fib2

    return fib2
