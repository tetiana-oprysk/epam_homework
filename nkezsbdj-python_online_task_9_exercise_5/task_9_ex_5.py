"""
Implement function count_letters, which takes string as an argument and
returns a dictionary that contains letters of given string as keys and a
number of their occurrence as values.

Example:
print(count_letters("Hello world!"))
Result: {'H': 1, 'e': 1, 'l': 3, 'o': 2, 'w': 1, 'r': 1, 'd': 1}

Note: Pay attention to punctuation.
"""


def count_letters(some_str: str):
    if not isinstance(some_str, str):
        raise TypeError('Wrong data type.')
    dictionary_alpha = {}
    list_of_alpha = [i for i in list(some_str) if i.isalnum()]
    for i in list_of_alpha:
        dictionary_alpha[i] = some_str.count(i)
    return dictionary_alpha
