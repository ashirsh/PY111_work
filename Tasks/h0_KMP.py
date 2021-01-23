from typing import Optional, List


def _prefix_fun(prefix_str: str) -> List[int]:
    """
    Prefix function for KMP

    :param prefix_str: dubstring for prefix function
    :return: prefix values table
    """
    pi = [0] * len(prefix_str)
    i, j = 1, 0
    while i < len(prefix_str):
        if prefix_str[i] == prefix_str[j]:
            pi[i] = j + 1
            i += 1
            j += 1

        else:
            if j == 0:
                i += 1
            else:
                j = pi[j-1]
    return pi


def kmp_algo(inp_string: str, substr: str) -> Optional[int]:
    """
    Implementation of Knuth-Morrison-Pratt algorithm

    :param inp_string: String where substr is to be found (haystack)
    :param substr: substr to be found in inp_string (needle)
    :return: index where first occurrence of substr in inp_string started or None if not found
    """

    pi = _prefix_fun(substr)
    i, j = 0, 0
    while i <= len(inp_string)-len(substr):
        if inp_string[i] == substr[j]:
            first_occurrence = i
            while j < len(substr):
                if inp_string[i] != substr[j]:
                    j = pi[j-1]
                    break
                i += 1
                j += 1
            else:
                return first_occurrence
        else:
            i += 1
    return None


if __name__ == '__main__':
    s = 'abcdabcabcdabcdab'
    print(_prefix_fun(s))
    print(kmp_algo(s, 'bc'))
