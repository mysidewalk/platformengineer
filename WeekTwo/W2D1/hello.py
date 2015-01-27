#!/usr/bin/python

# hello.py is useful for talking through the most basic
# introductory concepts of python:
#  basic syntax and indentation 
#  keywords, built-in types, and built-in constants
#  operators, built-in functions, and imports
#  Execution: interpreter vs. textfile

# import module example -- sys is very useful
import sys

# Programatically look at all functions 'sys' provides
# Bonus 1: help(sys) from an interpreter for a friendlier view
# Bonus 2: 
dir(sys)


# Organize our code in a main() function
def main():
   # (for example, 'hello.py')
    print 'Hello there!', sys.argv[1]

    # Command line args are in sys.argv[1], sys.argv[2] ...
    # sys.argv[0] shows the script name itself as it was called
   # (for example, 'hello.py')

def test():
    print "We ran the test() function instead of main."
    print "Python isn't set on having a main function run first."
    print "In python, naming conventions are strongly standardized..."
    print "... but loosely-enforced. The best of both worlds."

# Standard boilerplate to call an entry function 
# to begin the program when called like "python hello.py"
# This is utilizing something we'll talk in-depth about later on: "magic methods"
# Read more here: http://farmdev.com/src/secrets/magicmethod/
if __name__ == '__main__':
    main()
