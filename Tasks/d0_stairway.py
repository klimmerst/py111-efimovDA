from typing import Union, Sequence


def stairway_path(stairway: Sequence[Union[float, int]]) -> Union[float, int]:
    """
    Calculate min cost of getting to the top of stairway if agent can go on next or through one step.

    :param stairway: list of ints, where each int is a cost of appropriate step
    :return: minimal cost of getting to the top
    """

    if not stairway:
        return 0

    buf_1 = 0
    buf_2 = 0
    one_back = stairway[1]
    two_back = stairway[0]

    for i in range(2, len(stairway)):
        buf_1 = one_back + stairway[i]
        buf_2 = two_back + stairway[i]
        two_back = one_back
        if buf_1 < buf_2:
            one_back = buf_1
        else:
            one_back = buf_2

    if buf_1 < buf_2:
        return buf_1
    else:
        return buf_2