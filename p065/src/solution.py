'''
Created on Apr 28, 2012

@author: valentcraft

Copyright (c) 2012 Jun Mei

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
def expand_e(number_of_terms):
    (a0, b0) = (2, 1)
    (a1, b1) = (3, 1)
    for term in range(3, number_of_terms + 1):
        (q, r) = divmod(term, 3)
        k = (q << 1) if r == 0 else 1
        a2 = k * a1 + a0
        b2 = k * b1 + b0
        (a0, b0) = (a1, b1)
        (a1, b1) = (a2, b2)
    return (a1, b1)

if __name__ == '__main__':
    (a, b) = expand_e(100)
    result = sum([int(x) for x in str(a)])
    print(result)
