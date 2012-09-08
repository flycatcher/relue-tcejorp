'''
Created on Sep 7, 2012

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
import collections
import functools
import math

def sum_of_powers_of_minus_two(powers, limit):
    if len(powers) == 0:
        return 0
    exp_counts = collections.defaultdict(int)
    for p in powers:
        exp_counts[p] += 1
    num_items_remained, result = len(powers), 0
    exps = sorted(exp_counts.keys(), reverse=True)
    last_exp, log_limit = exps[0], math.log(limit, 2)
    for exp in exps:
        if not result == 0:
            # If the significant is non-zero, calculate the current running sum.
            # If it's not within the limit, and cannot be offset, return -1.
            log_result = last_exp + math.log(math.fabs(result), 2)
            if log_result > log_limit and log_result > exp + math.log(num_items_remained, 2):
                return -1
        result = result << (last_exp - exp)
        counts, last_exp = exp_counts[exp], exp
        num_items_remained -= counts
        result += counts if (exp & 1) == 0 else -counts
    result = result << last_exp
    return result if math.fabs(result) < limit else -1

def sum_of_powers_of_minus_two_bruteforce(powers, limit):
    result = functools.reduce(lambda x, y: x + (-2) ** y, powers, 0)
    return result if math.fabs(result) < limit else -1

if __name__ == '__main__':
    limit = 10000000
    tests = list()
    tests.append([])
    tests.append([0])
    tests.append([1])
    tests.append([0, 2, 3, 1])
    tests.append([2, 2, 2, 2])
    tests.append([2, 2, 2, 43])
    tests.append([2, 8, 12, 2, 3, 4, 5, 6])
    tests.append([2, 2, 2, 43, 42, 41, 40, 40, 40])
    tests.append([34, 123, 1, 2, 1, 0, 1, 0, 5, 6, 1])
    tests.append([2, 2, 2, 2, 2, 8, 12, 2, 3, 3, 3, 4, 3, 3, 3, 3, 3, 5, 6, 11])
    tests.append([34, 123, 1, 2, 1, 0, 1, 0, 5, 6, 1, 120, 120, 33, 33, 120, 120, 120, 120, 120, 120])
    for test in tests:
        left = sum_of_powers_of_minus_two(test, limit)
        right = sum_of_powers_of_minus_two_bruteforce(test, limit)
        assert left == right
    print('Tests Passed')
