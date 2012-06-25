'''
Created on Jun 24, 2012

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
import fractions

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
    ans, primes = 0, sp(10 ** 5)
    for p in primes:
        is_factor, m, phi = False, 9 * p, p - 1
        k_max = int(math.log(phi, 2) + 2)
        for k in range(1, k_max):
            # 10^n - 1 is divisible by prime p if and only if 10^phi(p) - 1 is
            # divisible by p. As 10^n = 10^phi(p) = 1 (mod p), this equivalence
            # holds true if and only if 10^gcd(n, phi(p)) = 1 (mod p).  
            d = fractions.gcd(10 ** k, phi)
            if pow(10, d, m) == 1:
                is_factor = True
                break
        if not is_factor:
            ans += p
    print(ans)
