'''
Created on Jul 13, 2012

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

def sieve_primes(limit):
    """
    Returns all prime numbers less than or equal to the given upper bound; this
    method implements the Sieve of Atkin for prime generation.
    """
    if limit < 2:
        return []
    (q, r) = divmod(limit, 2)
    lng = q + r - 1
    sieve = [True] * (lng + 1)
    for i in range(int(math.sqrt(limit)) >> 1):
        if not sieve[i]:
            continue
        inc = (i << 1) + 3
        for j in range((i * (i + 3) << 1) + 3, lng, inc):
            sieve[j] = False
    result = [2]
    result.extend([(i << 1) + 3 for i in range(lng) if sieve[i]])
    return result

def totient_chain(n):
    primes = sieve_primes(n)
    result = dict()
    while n > 2:
        totient = n
        m = (n >> 1)
        for x in primes:
            if x > m:
                break
            if (n % x) == 0:
                totient -= (totient // x)
        result.setdefault(n, totient)
        n = totient
    result.setdefault(1, 1)
    result.setdefault(2, 1)
    return result

def tetration(a, b, m):
    totients = totient_chain(m)
    hyper_exp = list()
    while b > 0:
        hyper_exp.append(m)
        m, b = totients[m], b - 1
    hyper_exp.reverse()
    result = a
    for n in hyper_exp:
        result = pow(a, result, n)
    return result

if __name__ == '__main__':
    ans = tetration(1777, 1854, 10 ** 8)
    print(ans)
