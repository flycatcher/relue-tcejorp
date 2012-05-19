'''
Created on May 19, 2012

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
import itertools

if __name__ == '__main__':
    powers = [x for x in range(6)]
    primes = [2, 3, 5, 7, 11, 13]
    primes.reverse()
    result = float('inf')
    for exp in itertools.product(powers, repeat=len(primes)):
        factors = 1
        for idx, prime in enumerate(primes):
            factors *= (2 * exp[idx] + 1)
        if factors > 2000:
            x = 1
            for idx, prime in enumerate(primes):
                x *= (prime ** exp[idx])
            if x < result:
                result = x
    print(result)
