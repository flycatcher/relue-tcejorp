'''
Created on Apr 30, 2012

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
import fractions
from math import floor

def pythagorean_triple(m, n):
    m_sq, n_sq = m ** 2, n ** 2
    if m > n:
        return (m_sq - n_sq, (m * n) << 1, m_sq + n_sq)
    else:
        return (n_sq - m_sq, (m * n) << 1, m_sq + n_sq)

def is_primitive(m, n):
    return (m - n) % 2 != 0 and fractions.gcd(m, n) == 1

def count_uniques(max_perimeter):
    counts = [0] * max_perimeter
    sqrt_perimeter = floor(max_perimeter ** 0.5)
    for m in range(2, sqrt_perimeter):
        n_start = 1 if m % 2 == 0 else 2
        for n in range(n_start, m, 2):
            if is_primitive(m, n) == False:
                continue
            (a, b, c) = pythagorean_triple(m, n)
            p = a + b + c
            for i in range(p, max_perimeter, p):
                counts[i] += 1
    result = 0
    for i in range(12, max_perimeter):
        if counts[i] == 1:
            result += 1
    return result

if __name__ == '__main__':
    result = count_uniques(1500001)
    print(result)
