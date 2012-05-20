'''
Created on May 20, 2012

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

References:

1. http://en.wikipedia.org/wiki/Factorial#Number_theory
'''
import math

def sieve_primes(upper_bound):
    sieve = [True] * upper_bound
    sqrt_ub = math.ceil(math.sqrt(upper_bound))
    for x in range(3, sqrt_ub, 2):
        if sieve[x] == False:
            continue
        for y in range(x << 1, upper_bound, x):
            sieve[y] = False
    result = [x for x in range(3, upper_bound, 2) if sieve[x]]
    if upper_bound > 1:
        result.append(2)
    return result

def factorial_sopfr(n, primes):
    result = 0
    for p in primes:
        m = p
        while m <= n:
            result += math.floor(n / m) * p
            m *= p
    return result

def binomial_sopfr(n, m):
    primes = sieve_primes(n + 1)
    result = factorial_sopfr(n, primes)
    result -= factorial_sopfr(m, primes)
    result -= factorial_sopfr(n - m, primes)
    return result

if __name__ == '__main__':
    ans = binomial_sopfr(20000000, 5000000)
    print(ans)
