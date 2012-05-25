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
import functools
import math
import multiprocessing

def sieve_odd_primes(limit, start=3):
    sieve = [True] * limit;
    sqrt_limit = int(math.sqrt(limit))
    for i in range(3, sqrt_limit, 2):
        if sieve[i]:
            for j in range(i ** 2, limit, i):
                sieve[j] = False
    result = [x for x in range(start, limit, 2) if sieve[x]]
    return result

def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)
        return (g, x - (b // a) * y, y)

def modinv(a, m):
    g, x, y = egcd(a, m) #@UnusedVariable
    if g != 1:
        raise Exception('modular inverse does not exist')
    else:
        return x % m

def cal_s(p):
    # (p - 1)! = -1 (mod p) [Wilson's theorem]
    # (p - 2)! = 1 (mod p)
    # (p - 3)! = (p - 2)^(-1) (mod p) = (-1)*2^(-1) (mod p)
    # (p - 4)! = (p - 3)^(-1) * (p - 3)! (mod p) = 6^(-1) (mod p)
    # (p - 5)! = (p - 4)^(-1) * (p - 4)! (mod p) = (-1)*(24)^(-1) (mod p)
    # => sum = (-3)*8^(-1) (mod p)
    return ((-3) * (modinv(8, p))) % p

if __name__ == '__main__':
    primes = sieve_odd_primes(10 ** 8, start=5)
    pool = multiprocessing.Pool(4)
    result = pool.map(cal_s, primes)
    ans = functools.reduce(lambda x, y: x + y, result)
    print(ans)
