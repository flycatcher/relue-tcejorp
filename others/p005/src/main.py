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

def equi(a):
    size = len(a)
    if not size:
        return -1
    if size == 1:
        return 0
    counter, running_sum = 0, list()
    for v in a:
        counter += v
        running_sum.append(counter)
    full_sum = running_sum[-1]
    for idx in range(size):
        left = running_sum[idx - 1] if idx > 0 else 0
        if full_sum == 2 * left + a[idx]:
            return idx
    return -1

if __name__ == '__main__':
    tests = []
    tests.append(([], -1))
    tests.append(([0], 0))
    tests.append(([1], 0))
    tests.append(([1 << 32], 0))
    tests.append(([-1, 0], 0))
    tests.append(([0, 0, 1, -1], 0))
    tests.append(([1, 0, 1, -1], 0))
    tests.append(([0, 1, 1, -1], 1))
    tests.append(([1 << 32, -(1 << 32), 34], 2))
    for (a, expected_result) in tests:
        result = equi(a)
        assert result == expected_result
    print('Tests Passed')
