'''
Created on May 27, 2012

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
import math

def sod(x, m=10):
    result = 0
    while x > 0:
        (x, r) = divmod(x, m)
        result += r
    return result

def expand_series(n):
    result = []
    for x in range(2, 9 * n + 10):
        log10_x = math.log10(x)
        for e in range(math.ceil(n / log10_x), math.ceil((n + 1) / log10_x)):
            m = x ** e
            if sod(m) == x:
                result.append(m)
    result.sort()
    return result

if __name__ == '__main__':
    series = []
    n, m = 1, 30
    while len(series) < m:
        series.extend(expand_series(n))
        n += 1
    print(series[m - 1])
