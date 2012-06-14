'''
Created on Jun 13, 2012

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

1. http://oeis.org/A018892
'''
import copy
import functools
import itertools

def to_int(facts):
    """
    Assuming the input is a list of tuples of the form (p_i, a_i), this method
    returns the scalar product (p_i ** a_i) * (p_j ** a_j) * ...
    """
    result = functools.reduce(lambda x, y: x * (y[0] ** y[1]), facts, 1)
    return result

def divisors(e):
    """
    Assuming that integer n can be factorized as p0^a0 * p1^a1 * ... where the
    exponents [a0, a1, ...] are provided in the input argument, this method
    returns the number of divisors for n^2
    """
    result = functools.reduce(lambda x, y: x * (2 * y + 1), e, 1)
    return result

if __name__ == '__main__':
    primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53]
    exponents, limit = [1] * 15, 8 * (10 ** 6)
    ans = to_int(zip(primes, exponents))
    while len(exponents) > 5:
        exponents.pop()
        tmp = copy.copy(exponents)
        for exp_add in itertools.product(range(3), repeat=5):
            u = copy.copy(tmp)
            for i, v in enumerate(exp_add):
                u[i] += v
            if divisors(u) > limit:
                m = to_int(zip(primes, u))
                if m < ans:
                    ans, exponents = m, u
    print(ans)
