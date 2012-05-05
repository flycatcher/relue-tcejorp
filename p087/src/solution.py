'''
Created on May 4, 2012

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
import itertools
import math

def sieve_primes(upper_bound):
    sieve = [True] * upper_bound
    for i in range(4, upper_bound, 2):
        sieve[i] = False
    for i in range(3, upper_bound, 2):
        if sieve[i]:
            for j in range(i << 1, upper_bound, i):
                sieve[j] = False
    return [x for x, is_prime in enumerate(sieve) if x > 1 and is_prime]

def count(upper_bound):
    primes = sieve_primes(math.ceil(upper_bound ** 0.5))
    squares = [x ** 2 for x in primes if x ** 2 < upper_bound]
    cubes = [x ** 3 for x in primes if x ** 3 < upper_bound]
    zenzizenzics = [x ** 4 for x in primes if x ** 4 < upper_bound]
    expressables = set()
    for (sq, cu, ze) in itertools.product(squares, cubes, zenzizenzics):
        x = sq + cu + ze
        if x < upper_bound:
            expressables.add(x)
    result = len(expressables)
    return result

if __name__ == '__main__':
    ans = count(50000000)
    print(ans)
