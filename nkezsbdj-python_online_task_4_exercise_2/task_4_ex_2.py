"""
Task04_1_2
Write `is_palindrome` function that checks whether a string is a palindrome or not
Returns 'True' if it is palindrome, else 'False'

To check your implementation you can use strings from here
(https://en.wikipedia.org/wiki/Palindrome#Famous_palindromes).

Note:
Usage of any reversing functions is prohibited.
The function has to ignore special characters, whitespaces and different cases
Raise ValueError in case of wrong data type
"""


def is_palindrome(test_string: str) -> bool:
    try:
        lower_string = test_string.lower()
        new_string = ''.join(i for i in lower_string if i.isalnum())
        if new_string == new_string[::-1]:
            return True
        else:
            return False
    except:
        raise ValueError