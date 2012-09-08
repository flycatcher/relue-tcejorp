'''
Created on Sep 7, 2012

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

def array_jump(a):
    result, limit, idx_fast, idx_slow = 0, len(a), 0, 0
    while 0 <= idx_fast and idx_fast < limit:
        idx_slow += a[idx_slow]
        idx_fast += a[idx_fast]
        result += 1
        if 0 <= idx_fast and idx_fast < limit:
            idx_fast += a[idx_fast]
            result += 1
            if idx_fast == idx_slow:
                return -1
    return result

if __name__ == '__main__':
    tests = []
    tests.append(([], 0))
    tests.append(([1], 1))
    tests.append(([-1, 10], 1))
    tests.append(([2, 3, 1, 1, 3], 4))
    tests.append(([2, 3, 1, -1, 3], -1))
    tests.append(([2, 3, 1, 0, 0, 4, -1, 3], -1))
    tests.append(([2, 3, 1, -10, 0, -1, 3], 3))
    tests.append(([2, 3, 1, -3, 0, -1, 3], -1))
    for (a, expected_result) in tests:
        result = array_jump(a)
        assert result == expected_result
    print('Tests Passed')
