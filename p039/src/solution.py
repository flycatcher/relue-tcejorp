'''
Created on Apr 20, 2012

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
import itertools
import math

if __name__ == '__main__':
    max_perimeter = 1000
    squares = [x ** 2 for x in range(1, max_perimeter >> 1)]
    square_set = set(squares)
    counts = {}
    for (a_sq, b_sq) in itertools.combinations(squares, 2):
        c_sq = a_sq + b_sq
        if c_sq in square_set:
            p = math.sqrt(c_sq) + math.sqrt(a_sq) + math.sqrt(b_sq)
            if p < max_perimeter:
                p = math.floor(p)
                counts.setdefault(p, 0)
                counts[p] += 1
    result = max(counts, key=counts.get)
    print(result)
