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

def decimal_size(n):
    result = math.ceil(math.log10(n + 0.5))
    return result

def integer_decimal_occurrence(a, b):
    if a == 0 and b == 0:
        return 0
    size_a, size_b = decimal_size(a), decimal_size(b)
    mask = int(10 ** size_a + 0.5)
    result, idx = -1, size_b - size_a
    while b > 0 and a <= b:
        if (b - a) % mask == 0:
            result = idx
        b = b // 10
        idx -= 1
    return result

if __name__ == '__main__':
    tests = []
    tests.append((53, 1953786, 2))
    tests.append((78, 195378678, 4))
    tests.append((57, 153786, -1))
    tests.append((0, 103706, 1))
    tests.append((10, 103706, 0))
    tests.append((103, 103103, 0))
    tests.append((111, 11111111111, 0))
    tests.append((19, 11111991111119, 4))
    tests.append((19, 0, -1))
    for (a, b, expected_result) in tests:
        result = integer_decimal_occurrence(a, b)
        assert result == expected_result
    print('Tests Passed')
