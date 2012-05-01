'''
Created on Apr 26, 2012

Copyright (c) 2012, Jun Mei

Permission is hereby granted, free of charge, to any person obtaining a copy of
this software and associated documentation files (the "Software"), to deal in
the Software without restriction, including without limitation the rights to
use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of
the Software, and to permit persons to whom the Software is furnished to do so,
subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS
FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR
COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER
IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN
CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
'''
from math import floor, log10
import sys

def count_expansions(number_of_terms):
    result = 0
    a = 1
    b = 1
    for term in range(0, number_of_terms): #@UnusedVariable
        a_next = a + (b << 1)
        b_next = a + b
        if floor(1 + log10(a_next)) > floor(1 + log10(b_next)):
            result += 1
        a = a_next
        b = b_next
    return result

if __name__ == '__main__':
    number_of_terms = int(sys.argv[1]) if len(sys.argv) > 1 else 1000
    result = count_expansions(number_of_terms)
    print(result)
