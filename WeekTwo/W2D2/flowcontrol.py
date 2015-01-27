#!/usr/bin/python

'''
MindMixer Platform Engineer Training - Part 1
W2D2 - flow control, sequences, and iterables

Exercises related to: Control Flow Structures

Pro-tip: run a specific function from the command line directly like so:
python -c 'import this_filename; my_function(a_parameter,b_parameter)'
(you must be in the directory where "this_filename.py" resides)

'''

# Place any needed module imports here...
# Example: import modulename as mn

# Please see the "Control Flow Structures Exercises" portion of
# pairedexercises.md from today's class directory for further information.

def inhabitant_growth(x,y):
    '''
    Use a for loop to solve the following problem:
    The country of Swaziland has X inhabitants, and its population
    grows 3% per year. The nation of Djibouti has a population of Y
    and grows 2% per year. Return in how many years Swaziland will
    surpass Djibouti.
    '''
    x_growth = 1.03
    y_growth = 1.02

#    i = 0
#    while x <= y:
#        x = x * x_growth
#        y = y * y_growth
#        i += 1
#    print i, "years surpassed"

    i = 0
    for i in range(1,100000):
        x = x * x_growth
        y = y * y_growth
        if x > y:
            print i, "years have surpassed"
            break;
        i += 1


def hello_datetime_world(num_of_seconds):
    '''
    Use a while loop to print "Hello world!" for ~3 seconds.
    '''
    import datetime as dt
    end_time = dt.datetime.now() + dt.timedelta(seconds=num_of_seconds)
    while True:
        if dt.datetime.now() >= end_time:
            print "Time surpassed"
            break;
        print "Hellooooo world!"

def hello_timed_world(num_of_seconds):
    import time
    end_time = time.time() + num_of_seconds
    start_time = time.time()
    while True:
        if time.time() >= end_time:
            print start_time - time.time(), "seconds surpassed. Breaking..."
            break;
        print "Hello world!"

def bad_grades(grade_value):
    '''
    Use 'if'/'elif'/'else' statements to return a letter grade
    based on a 0-100 integer input. Be sure to allow for at least
    two significant digits after the decimal point.

    Cut-offs for each letter shall be as follows:

    A = Greater than or equal to 90
    B = 80 to 89
    C = 70 to 79
    D = 60 to 69
    F = Less than but not equal to 60
    '''
    gv = grade_value

    if gv >= 90:
        print "A"
    elif gv in range(80,90):
        print "B"
    elif gv in range(70,80):
        print "C"
    elif gv in range(60,70):
        print "D"
    elif gv < 60:
        print "Fail."
    else:
        "Not sure."

def main():
    '''
    For extra points, modify this main function to call your
    other completed functions.

    You may statically define the function parameters that are
    passed in for each function call, or utilize a module to
    grab arbitrary parameters from the command line invocation.

    Either is perfectly valid.
    '''


# Keep this as-is to invoke main.
if __name__ == '__main__':
    main()
