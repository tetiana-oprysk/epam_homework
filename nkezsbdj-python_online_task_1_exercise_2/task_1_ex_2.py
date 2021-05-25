import argparse
import math
import operator

parser = argparse.ArgumentParser()
parser.add_argument('operators', nargs='*')


def calculation(args):
    num_1 = float(args.operators[1])
    sign = args.operators[0]
    if len(args.operators) == 3:
        num_2 = float(args.operators[2])
        if sign in dir(math):
            return getattr(math, sign)(num_1, num_2)
        elif sign in dir(operator):
            return getattr(operator, sign)(num_1, num_2)
        else:
            raise NotImplementedError('It`s non-mathematical function.')
    elif len(args.operators) == 2:
        if sign in dir(math):
            return getattr(math, sign)(num_1)
        elif sign in dir(operator):
            return getattr(operator, sign)(num_1)
        else:
            raise NotImplementedError('It`s non-mathematical function.')
    else:
        raise Exception('Error')


def main():
    args = parser.parse_args()
    print(calculation(args))


if __name__ == '__main__':
    main()
