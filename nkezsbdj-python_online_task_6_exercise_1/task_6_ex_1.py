"""
Implement function combine_dicts, which receives a changeable
number of dictionaries (keys - letters, values - integers)
and combines them into one dictionary.

Dict values should be summarized in case of identical keys.

Example:
dict_1 = {'a': 100, 'b': 200}
dict_2 = {'a': 200, 'c': 300}
dict_3 = {'a': 300, 'd': 100}

combine_dicts(dict_1, dict_2)
Result: {'a': 300, 'b': 200, 'c': 300}

combine_dicts(dict_1, dict_2, dict_3)
Result: {'a': 600, 'b': 200, 'c': 300, 'd': 100}
"""


def combine_dicts(*args):
    new_dict = dict()
    if any(not isinstance(key, str) or not key.isalpha() or len(key) > 1 for arg in args for key in arg.keys()):
        raise KeyError
    if any(not isinstance(value, int) or value <= 0 for arg in args for value in arg.values()) \
            or any(not isinstance(arg, dict) or arg is None for arg in args):
        raise ValueError

    for arg in args:
        for key, value in arg.items():
            if key in new_dict.keys():
                new_dict[key] = new_dict[key] + value
            else:
                new_dict[key] = value
    return new_dict
