'''
Created on Jun 14, 2012

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

References:

1. http://en.wikipedia.org/wiki/Permutation#Generation_in_lexicographic_order
'''
import functools
import itertools
import math

def next_permutation(lst):
    """
    Updates the given list to the next lexicographic permutation by value;
    returns True if the list is successfully updated, False otherwise 
    """
    k = -1
    for i in range(len(lst) - 1, 0, -1):
        if lst[i - 1] < lst[i]:
            k = i - 1
            break
    if k < 0:
        return False
    l, a_k = k + 1, lst[k]
    for i in range(len(lst) - 1, k, -1):
        if lst[i] > a_k:
            l = i
            break
    lst[k], lst[l] = lst[l], a_k
    tail = lst[k + 1:]
    tail.reverse()
    lst[k + 1:] = tail
    return True

def is_prime(n):
    """
    Determines if the given integer is a prime number
    """
    if n == 2:
        return True
    if (n & 1) == 0:
        return False
    m = int(math.sqrt(n)) + 1
    for k in range(3, m, 2):
        if (n % k) == 0:
            return False
    return True

def maxiprimes(num_digits, d):
    result = 0
    fillers = [x for x in range(10) if not x == d]
    for m in range(num_digits, 0, -1):
        digits = [d] * m
        for o in itertools.combinations_with_replacement(fillers, r=num_digits - m):
            p = list(o)
            p.extend(digits)
            p.sort()
            while True:
                if p[0] > 0:
                    n = functools.reduce(lambda x, y: (x * 10) + y, p)
                    if is_prime(n):
                        result += n
                if not next_permutation(p):
                    break
        if result > 0:
            break
    return result

if __name__ == '__main__':
    ans = functools.reduce(lambda x, y: x + maxiprimes(10, y), range(10), 0)
    print(ans)
