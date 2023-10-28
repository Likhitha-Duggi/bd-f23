#!/usr/bin/env python

"""This program takes lines of text as input, where each line contains one or more values.
 It tries to extract and output numeric values while ignoring non-numeric values."""


import sys

for line in sys.stdin: # look through data that is piped into this program
    line = line.strip() # removes leading and trailing white spaces
    values = line.split() # Splits the line into list of values

    for value in values:
        try:
            numeric_val = float(value) #Tries to convert value to float - example 2 is converted to 2.0
            print '%s\t%s' % ('NUMERIC', numeric_val)

        except ValueError:
            # Ignore non-numeric values by using pass statement
            pass


