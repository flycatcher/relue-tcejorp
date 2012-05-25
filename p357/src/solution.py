'''
Created on May 24, 2012

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

def sieve_odd_primes(limit):
    sieve = [True] * limit;
    sqrt_limit = int(math.sqrt(limit))
    for i in range(3, sqrt_limit, 2):
        if sieve[i]:
            for j in range(i << 1, limit, i):
                sieve[j] = False
    result = set(x for x in range(3, limit, 2) if sieve[x])
    return result

def find_candidates(primes):
    result = []
    squares = sorted(x ** 2 for x in primes)
    for prime in primes:
        n = prime - 1
        if n % 4 == 0 or (2 + (n >> 1)) not in primes:
            continue
        is_squarefree = True
        for sq in squares:
            if sq > n:
                break
            elif n % sq == 0:
                is_squarefree = False
                break
        if is_squarefree:
            result.append(n)
    return result

def check_divisors(n, primes):
    sqrt_n = int(math.sqrt(n))
    for i in range(3, sqrt_n):
        (q, r) = divmod(n, i)
        if r == 0 and (q + i) not in primes:
            return 0
    return n

if __name__ == '__main__':
    primes = sieve_odd_primes(100000000)
    candidates = find_candidates(primes)
    result = map(lambda x: check_divisors(x, primes), candidates)
    ans = sum(result) + 1 # Special case: 1 + 1 = 2 (prime)
    print(ans)
