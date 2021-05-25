"""
Implement a decorator remember_result which remembers last result of function it decorates
and prints it before next call.

@remember_result
def sum_list(*args):
    result = ""
    for item in args:
        result += str(item)
    print(f"Current result = '{result}'")
    return result

sum_list("a", "b")
#>>> "Last result = 'None'"
#>>> "Current result = 'ab'"

sum_list("abc", "cde")
#>>> "Last result = 'ab'"
#>>> "Current result = 'abccde'"

sum_list(3, 4, 5)
#>>> "Last result = 'abccde'"
#>>> "Current result = '345'"
"""
arr = []


def remember_result(fn):
    def wrapper(*args):
        if len(arr) == 0:
            print(f"Last result = '{None}'")
        else:
            print(f"Last result = '{arr[-1]}'")
        a = fn(*args)
        arr.append(a)
        return a
    return wrapper


@remember_result
def sum_list(*args):
    result = ""
    for item in args:
        result += str(item)
    print(f"Current result = '{result}'")
    return result
