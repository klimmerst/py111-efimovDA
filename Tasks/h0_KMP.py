from typing import Optional, List


def _prefix_fun(prefix_str: str) -> List[int]:
    """
    Prefix function for KMP

    :param prefix_str: dubstring for prefix function
    :return: prefix values table
    """
    len_pref = len(prefix_str)
    prefix = [0 for i in range(len_pref)]
    j = 0
    i = 1
    
    while i < len_pref:
        
        if prefix_str[i] == prefix_str[j]:
            prefix[i] = j + 1
            i += 1
            j += 1
        else:
            if j != 0:
                j = prefix[j - 1]
            else:
                prefix[i] = 0
                i += 1

    return prefix


def kmp_algo(inp_string: str, substr: str) -> Optional[int]:
    """
    Implementation of Knuth-Morrison-Pratt algorithm

    :param inp_string: String where substr is to be found (haystack)
    :param substr: substr to be found in inp_string (needle)
    :return: index where first occurrence of substr in inp_string started or None if not found
    """
    len_sub = len(substr)
    len_inp = len(inp_string)

    pref = _prefix_fun(substr)
    j = 0
    i = 0

    while i < len_inp and j < len_sub:

        if substr[j] == inp_string[i]:
            i += 1
            j += 1
        elif j == 0:
            i += 1
        else:
            j = pref[j - 1]

    if j == len_sub:
        return i - j

    return None
