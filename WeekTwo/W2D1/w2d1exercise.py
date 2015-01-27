#!/usr/bin/python

# Complete the function below and any other aspects
# required to print an arbitrary first and last name entered from the command
# Also print the length of the first and last name separately on two new lines

import sys

# Example input: python script.py Dan Fowler
# Example output:
# Dan
# Fowler
# 3
# 6

def test(filename,*args):

# Additionally, make any changes required to ensure this function is immediately called
# when the python file is invoked from a command line.

if __name__ == '__main__':
    test(sys.argv[0],sys.argv[1:-1])

