#!/usr/bin/python

'''
MindMixer Platform Engineer Training - Part 1
W2D2 - flow control, sequences, and iterables

Pro-tip: run a specific function from the command line directly like so:
python -c 'import this_filename; my_function(a_parameter,b_parameter)'
(you must be in the directory where "this_filename.py" resides)

'''

# Place our imports here...


# Some variables of various types so we can save time typing
# example input each time we run a function. Named accordingly.
ex_string  = "An example string"
ex_integer = 15
ex_list    = [1,'one','another item',15]
ex_tuples  = [(1,1),(2,4),(3,9),(4,16)]


# Below are several functions illustrating various methods for controlling flow
# of your programs in Python. This is a brief overview and far from definitive.
# More here: http://en.wikibooks.org/wiki/Python_Programming/Control_Flow


# Example 1: if statements
# Simple if statement with elif and else.
# Only accepts integers.
def control_flow_if(ex_integer):
    if isinstance(ex_integer,int):
        if ex_integer > 0:
            print "Value was Positive"
        elif ex_integer == 0:
            print "Value was Zero"
        elif ex_integer < 0:
            print "Value was Negative"
    else:
        print "I don\'t think you entered an integer..."

# Example 2: 'for' loops
# Simple 'for' loop iterating over an arbitrary input
# each element of the list (i.e. each letter in a string)
def control_flow_simple_for(ex_string):
    for i in ex_string:
        print i

# Example 3: More 'for' loops with multi-tuple list
# Definition: Loops through a list of two-element tuples
# Note: A tuple is simply an immutable (unchangeable) list
#   Tuples are defined with parentheses "()"
#   Lists are defined with brackets "[]"
def control_flow_tuple_for(ex_tuples):
    for i, isquared in ex_tuples:
        print "At list item number:", ex_tuples[i]+1, "First tuple element"

# Example 4: 'while' loops
# A function illustrating various usages of controlling flow
# with python's built-in control flow statements
def flow_control(ex_integer):
    for i in range(ex_integer):
        print "This print loops should run " + str(ex_integer) + " times."

# A function illustrating usage of var
def show_range():
    return 0

# Usage message if invoked without function explicitly called
def main():
    print "This python module is designed for use within the interactive"
    print "interpreter as part of a larger teaching series."
    print "Please view the repo on GitHub for more info:"
    print "https://github.com/dannykansas/platformengineer"

# Again, ignore this for now (unless you want to change the default function
# invocation from main() to something else...)
if __name__ == '__main__':
    main()
