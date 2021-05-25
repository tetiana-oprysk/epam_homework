"""
Task 3

Implement a decorator `call_once` which runs `sum_of_numbers` function once and caches the result.
All consecutive calls to this function should return cached result no matter the arguments.

Example:
@call_once
def sum_of_numbers(a, b):
    return a + b

print(sum_of_numbers(13, 42))

#>>> 55

print(sum_of_numbers(999, 100))

#>>> 55

print(sum_of_numbers(134, 412))

#>>> 55
"""
data = []


def call_once(func):
    def wrapper(a, b):
        try:
            decimal = func(a, b)
            data.append(decimal)
            return data[0]
        except TypeError:
            return data[0]
    return wrapper


@call_once
def sum_of_numbers(a, b):
    return a + b
