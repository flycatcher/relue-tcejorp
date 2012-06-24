'''
Created on Jun 23, 2012

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

1. http://en.wikipedia.org/wiki/Modular_multiplicative_inverse
'''
import math

def sp(limit):
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

if __name__ == '__main__':
    p_last, p1, ans = 10 ** 6, 5, 0
    primes = sp(p_last + 10)
    for p in primes:
        if p <= p1:
            continue
        if p1 > p_last:
            break
        m = 10 ** int(math.log10(p1) + 1)
        phi = m
        phi -= phi // 2
        phi -= phi // 5
        p_inv = pow(p, phi - 1, m) # Euler's theorem
        ans += ((p_inv * p1) % m) * p
        p1 = p
    print(ans)
