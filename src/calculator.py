
import argparse
parser = argparse.ArgumentParser()
parser.add_argument('arguments', metavar='N', type=int, nargs='+',
                   help='an integer for the accumulator')
args = parser.parse_args()
print(args.arguments)

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        raise ValueError('ei voi jakaa')
    return x / y

print(add(args.arguments[0], args.arguments[1]))