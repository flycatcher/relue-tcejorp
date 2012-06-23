'''
Created on Jun 22, 2012

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

1. http://oeis.org/A000864
'''
import math
import sys

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
    primes = sp(10 ** 5)
    p, total, ans = 5, 25, 0
    for q in primes:
        if q <= p:
            continue
        for n in range(p + 2, q - 1, 2):
            if n % 5 == 0: # GCD(n, 10) = 1
                continue
            if pow(10, n - 1, 9 * n) == 1:
                ans += n
                total -= 1
                if total == 0:
                    print(ans)
                    sys.exit()
        p = q
    print('Need to increase prime sieving upper bound')

