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
import random

def distinct(a):
    size = len(a)
    if not size:
        return 0
    if size == 1:
        return 1
    a.sort()
    result = 1
    for idx in range(1, size):
        if a[idx] != a[idx - 1]:
            result += 1
    return result

def distinct_set(a):
    distinct_values = set(x for x in a)
    return len(distinct_values)

def generate_test(size):
    test = [random.randint(-100000000, 100000000) for x in range(size)] #@UnusedVariable
    ans = distinct_set(test)
    return (test, ans)

if __name__ == '__main__':
    tests = []
    tests.append(generate_test(0))
    tests.append(generate_test(1))
    tests.append(generate_test(10))
    tests.append(generate_test(100))
    tests.append(generate_test(1000))
    tests.append(generate_test(10000))
    tests.append(generate_test(100000))
    tests.append(generate_test(10))
    tests.append(generate_test(100))
    tests.append(generate_test(1000))
    tests.append(generate_test(10000))
    tests.append(generate_test(100000))
    tests.append(generate_test(10))
    tests.append(generate_test(100))
    tests.append(generate_test(1000))
    tests.append(generate_test(10000))
    tests.append(generate_test(100000))
    tests.append(generate_test(10))
    tests.append(generate_test(100))
    tests.append(generate_test(1000))
    tests.append(generate_test(10000))
    tests.append(generate_test(100000))
    tests.append(generate_test(10))
    tests.append(generate_test(100))
    tests.append(generate_test(1000))
    tests.append(generate_test(10000))
    tests.append(generate_test(100000))
    for (a, expected_result) in tests:
        ans = distinct(a)
        if not ans == expected_result:
            print('{0}\nExpect={1} Actual={2}'.format(a, expected_result, ans))
        assert ans == expected_result
    print('Tests Passed')
