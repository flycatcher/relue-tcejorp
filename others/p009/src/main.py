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
import random

def abs_distinct(a):
    size = len(a)
    if not size:
        return 0
    if size == 1:
        return 1
    idx_head, idx_tail, result = 0, size - 1, 0
    while idx_head <= idx_tail:
        head, tail = math.fabs(a[idx_head]), math.fabs(a[idx_tail])
        # Each iteration visits a distinct number by absolute value
        result += 1
        if head > tail:
            # If head is greater than tail by absolute value, advance the head
            # to make it smaller.
            idx_head += 1
            # Skip duplicates
            while idx_head <= idx_tail and a[idx_head] == a[idx_head - 1]:
                idx_head += 1
        elif head < tail:
            # If tail is greater than head by absolute value, advance the tail
            # to make it smaller.
            idx_tail -= 1
            # Skip duplicates
            while idx_tail >= idx_head and a[idx_tail + 1] == a[idx_tail]:
                idx_tail -= 1
        else:
            # If head and tail are the same by absolute value, advance both.
            idx_head += 1
            idx_tail -= 1
            while idx_head <= idx_tail and a[idx_head] == a[idx_head - 1]:
                idx_head += 1
            while idx_tail >= idx_head and a[idx_tail + 1] == a[idx_tail]:
                idx_tail -= 1
    return result

def abs_distinct_set(a):
    s = set(int(math.fabs(x)) for x in a)
    return len(s)

def generate_test(size, r):
    test = sorted(random.randint(-r, r) for x in range(size)) #@UnusedVariable
    result = abs_distinct_set(test)
    return (test, result)

if __name__ == '__main__':
    tests = []
    tests.append(([], 0))
    tests.append(([1], 1))
    tests.append(([1, 1], 1))
    tests.append(([0, 1], 2))
    tests.append(([-1, 1], 1))
    tests.append(([-1, 1, 4], 2))
    tests.append(([-1, -1, -1, 0, 0, 0, 1, 1], 2))
    tests.append(([-1, 1, 4, 4, 4, 4], 2))
    tests.append(([-1, -1, -1, 0, 0, 0, 1, 1, 2, 2, 2, 2], 3))
    tests.append(([1, 1, 1, 1, 1, 2, 2, 2, 2, 2], 2))
    tests.append(([-2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2], 2))
    tests.append(([-2, 1, 1, 0, 0, 0, 0, 0, 1, 2, 2, 2], 3))
    tests.append(([-100, -2, -2, -2, -1, 0, 0, 1, 2, 2, 2], 4))
    tests.append(([-2, -2, -1, -1, -1, 0, 0, 0, 1, 1, 2, 2, 2, 2], 3))
    tests.append(generate_test(10, 1))
    tests.append(generate_test(10, 2))
    tests.append(generate_test(10, 3))
    tests.append(generate_test(20, 3))
    tests.append(generate_test(20, 4))
    for (a, expected_result) in tests:
        result = abs_distinct(a)
        if not result == expected_result:
            print(a)
            print('actual={0}, expected={1}'.format(result, expected_result))
        assert result == expected_result
    print('Tests Passed')
