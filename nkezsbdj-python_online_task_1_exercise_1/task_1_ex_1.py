import argparse
import operator

operators = {
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul,
    '/': operator.truediv,
}
parser = argparse.ArgumentParser()
parser.add_argument('first_number', help='First number to func', type=float)
parser.add_argument('operator', help='Operator')
parser.add_argument('second_number', help='Second number to func', type=float)


def calculation(num_1, chosen_operator, num_2):
    if chosen_operator in operators.keys():
        calc = operators[chosen_operator](num_1, num_2)
        return calc
    else:
        raise NotImplementedError('The operator you selected isn`t available for use')


def main():
    args = parser.parse_args()
    print(calculation(args.first_number, args.operator, args.second_number))


if __name__ == '__main__':
    main()
