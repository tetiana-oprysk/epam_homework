"""
Task 2_3

You are given n bars of gold with weights: w1, w2, ..., wn and bag with capacity W.
There is only one instance of each bar and for each bar you can either take it or not
(hence you cannot take a fraction of a bar). Write a function that returns the maximum weight of gold that fits
into a knapsack's capacity.

The first parameter contains 'capacity' - integer describing the capacity of a knapsack
The next parameter contains 'weights' - list of weights of each gold bar
The last parameter contains 'bars_number' - integer describing the number of gold bars
Output : Maximum weight of gold that fits into a knapsack with capacity of W.

Note:
Use the argparse module to parse command line arguments. You don't need to enter names of parameters (i. e. -capacity)
Raise ValueError in case of false parameter inputs
Example of how the task should be called:
python3 task3_1.py -W 56 -w 3 4 5 6 -n 4
"""
import argparse
from itertools import permutations

parser = argparse.ArgumentParser()
parser.add_argument('-W', type=int, dest='capacity', help='Max weight')
parser.add_argument('-w', type=int, dest='bars_weights', nargs='*', help='Bars weight')
parser.add_argument('-n', type=int, dest='bars_number', help='Bars number')


def bounded_knapsack(args):
    max_suma = 0
    for i in permutations(args.bars_weights, args.bars_number):
        suma = 0
        for j in range(args.bars_number):
            if args.capacity >= suma + i[j]:
                suma += i[j]
        if max_suma < suma:
            max_suma = suma
    return max_suma


def main():
    args = parser.parse_args()
    if not args.capacity:
        raise ValueError
    elif not args.bars_weights:
        raise ValueError
    elif not args.bars_number:
        raise ValueError
    elif len(args.bars_weights) == 0:
        raise ValueError
    elif args.capacity <= 0:
        raise ValueError
    elif args.bars_number <= 0:
        raise ValueError
    elif len(args.bars_weights) != args.bars_number:
        raise ValueError
    for i in args.bars_weights:
        if i > args.capacity:
            raise ValueError
        elif i <= 0:
            raise ValueError

    print(bounded_knapsack(args))


if __name__ == '__main__':
    main()
