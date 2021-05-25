"""
Task04_3

Implement a function which works the same as str.split

Note:
Usage of str.split method is prohibited
Raise ValueError in case of wrong data type
"""


def split_alternative(str_to_split: str, delimiter: str = ' ') -> list:
    split_str = []
    current_str = ''
    if not (isinstance(str_to_split, str) and isinstance(delimiter, str)):
        raise ValueError
    else:
        for i in str_to_split:
            if i == delimiter:
                split_str.append(current_str)
                current_str = ""
            else:
                current_str += i
        split_str.append(current_str)
        return split_str
