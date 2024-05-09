import sys
import argparse

print("hello world")

parser= argparse.ArgumentParser(description='Process some integers.')
parser.add_argument('integers', metavar='N', type=int, nargs='+',
                    help='an integer for the accumulator')


args = parser.parse_args()

print(args.integers)
print(sum(args.integers)
      )