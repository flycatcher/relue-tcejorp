'''
Created on Sep 8, 2012

Copyright (C) 2012, Jun Mei

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

def int_cubic_root(n):
    cubic_root = float(1) / 3
    result = math.pow(math.fabs(n) + 0.5, cubic_root)
    return -int(result) if n < 0 else int(result)

def whole_cubes_count(a, b):
    (lower_bound, upper_bound) = (a, b) if a < b else (b, a)
    cbrt_lower_bound = int_cubic_root(lower_bound)
    cbrt_upper_bound = int_cubic_root(upper_bound)
    result = cbrt_upper_bound - cbrt_lower_bound
    if upper_bound <= 0 and cbrt_upper_bound ** 3 == upper_bound:
        result += 1 # Include upper bound if it's a perfect cube
    elif lower_bound >= 0 and cbrt_lower_bound ** 3 == lower_bound:
        result += 1 # Include lower bound if it's a perfect cube
    elif upper_bound > 0 and lower_bound < 0:
        result += 1 # Include 0
    return result

if __name__ == '__main__':
    tests = []
    tests.append((1, 1, 1))
    tests.append((-1, -1, 1))
    tests.append((0, 0, 1))
    tests.append((1, 0, 2))
    tests.append((2, -1, 3))
    tests.append((0, 100, 5))
    tests.append((2, 100, 3))
    tests.append((-64, 100, 9))
    tests.append((-64, 64, 9))
    tests.append((-65, 100, 9))
    tests.append((-63, 100, 8))
    tests.append((-63, -8, 2))
    for (a, b, expected_result) in tests:
        result = whole_cubes_count(a, b)
        assert result == expected_result
    print('Tests Passed')
