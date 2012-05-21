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

def count_primes(n):
    primes = sieve_primes(n)
    result = 0
    for prime in primes:
        # For n^3 + p*(n^2) to be a cubic number, n needs to be cubic itself,
        # as well as (n + p). Let n = a^3. It follows that p = 3*a^2 + 3*a + 1.
        # Thus, a = [sqrt(12*p - 3) - 3] / 6. Since "a" needs to be a natural
        # number, (12*p - 3) must be a perfect square, sqrt(12*p - 3) needs to 
        # be divisible by 3 and greater than or equal to 9.
        d = 12 * prime - 3
        d_sqrt = math.floor(math.sqrt(d))
        if d_sqrt ** 2 == d and d_sqrt >= 9 and d_sqrt % 3 == 0:
            result += 1
    return result

if __name__ == '__main__':
    ans = count_primes(1000000)
    print(ans)
