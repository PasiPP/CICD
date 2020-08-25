
# import argparse
# parser = argparse.ArgumentParser()
# parser.add_argument('arguments', metavar='N', type=int, nargs='+',
#                    help='an integer for the accumulator')
# args = parser.parse_args()
# print(args.arguments)

def add(x, y):
    return x + y

if __name__ == "__main__":
    print(f'Tulostetaan {add(1,2)}')
# print(add(args.arguments[0], args.arguments[1]))