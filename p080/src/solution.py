'''
Created on May 3, 2012

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
from math import floor
import decimal

def sum_sqrt_digits(x, num_digits, scale):
    decimal.getcontext().prec = scale
    x_sqrt = decimal.Decimal(x).sqrt()
    offset = ord('0')
    result = sum((ord(c) - offset) for c in str(x_sqrt).replace('.', '', 1)[:num_digits])
    return result

if __name__ == '__main__':
    upper_bound = 100
    upper_bound_sqrt = floor(upper_bound ** 0.5)
    perfect_squares = set([x ** 2 for x in range(1, upper_bound_sqrt + 1)])
    ans = 0
    for x in range(1, upper_bound + 1):
        if x not in perfect_squares:
            ans += sum_sqrt_digits(x, 100, 110)
    print(ans)
