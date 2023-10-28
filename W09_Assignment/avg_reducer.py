#!/usr/bin/env python

"""This program received a stdin in pipe from mappers. It receives key-value pairs produced by the mapper, 
calculates the average of the numeric values, and outputs the result"""

import sys

# sum - to calculate sum of numbers in .txt file
# count - to count number of numeric entries in .txt file
sum = 0
count = 0

for line in sys.stdin:
    line = line.strip() #removes leading and trailing whitespaces
    key, value = line.split() #the line is split into 2 parts using whitespace as delimiter.
    # key represents type of data, value is data itself

    if key == 'NUMERIC':
        numeric_val = float(value)
        sum += numeric_val
        count += 1

if count > 0:
    average = sum / count
    print '%s\t%s' % ('AVERAGE=', average)

