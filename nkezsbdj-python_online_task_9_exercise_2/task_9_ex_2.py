"""
Write a function that checks whether a string is a palindrome or not.
Return 'True' if it is a palindrome, else 'False'.

Note:
Usage of reversing functions is required.
Raise ValueError in case of wrong data type

To check your implementation you can use strings from here
(https://en.wikipedia.org/wiki/Palindrome#Famous_palindromes).
"""


def is_palindrome(test_string: str) -> bool:
    if not isinstance(test_string, str):
        raise ValueError('Wrong data type.')
    reversed_str_list = reversed(test_string)
    lower_str_without_signs = ''.join(i.lower() for i in list(test_string) if i.isalnum())
    reversed_str_str = ''.join(i.lower() for i in list(reversed_str_list) if i.isalnum())
    return True if reversed_str_str == lower_str_without_signs else False
