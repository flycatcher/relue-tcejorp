'''
Created on Jul 4, 2012

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

def sum_digits(n):
    """
    Returns the sum of digits in the base-10 representation of the given integer
    """
    result = 0
    while n > 0:
        (n, r) = divmod(n, 10)
        result += r
    return result

def ones(n):
    '''
    Returns the number of 1s in the binary representation of the given integer
    '''
    result = 0
    while n > 0:
        result += (n & 1)
        n = n >> 1
    return result

def savings(n, codec):
    result = 0
    while n >= 10:
        n_next = sum_digits(n)
        for (s1, s2) in zip(str(n)[::-1], str(n_next)[::-1]):
            d1, d2 = codec.get(s1, 0), codec.get(s2, 0)
            result += (ones(d1 & d2) << 1)
        n = n_next
    return result

if __name__ == '__main__':
    primes = sp((10 ** 7) << 1)
    ans, lower_bound = 0, 10 ** 7
    codec = {
        '0': int('1111110', 2),
        '1': int('0011000', 2),
        '2': int('0110111', 2),
        '3': int('0111101', 2),
        '4': int('1011001', 2),
        '5': int('1101101', 2),
        '6': int('1101111', 2),
        '7': int('1111000', 2),
        '8': int('1111111', 2),
        '9': int('1111101', 2)
    }
    for p in primes:
        if p < lower_bound:
            continue
        ans += savings(p, codec)
    print(ans)
