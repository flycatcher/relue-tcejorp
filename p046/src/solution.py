'''
Created on Apr 22, 2012

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
import sys

def list_squares(number):
    upperbound = math.floor(math.sqrt(number / 2)) + 1
    return [(x ** 2) << 1 for x in range(1, upperbound)]

def list_primes(number):
    sieve = [True] * number
    for x in range(2, number):
        if sieve[x]:
            for y in range(2 * x, number, x):
                sieve[y] = False
    return [x for x in range(2, number) if sieve[x]]

def main(number):
    primes = list_primes(number)
    prime_set = set(primes)
    square_set = set(list_squares(number))
    for x in range(9, number, 2):
        if x in prime_set:
            continue
        is_found = True
        for prime in primes:
            y = x - prime
            if y < 2: # Bingo!
                break
            elif y in square_set:
                is_found = False
                break
        if is_found:
            print(x)
            sys.exit(0)

if __name__ == '__main__':
    main(10000)
