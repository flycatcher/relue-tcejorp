"""
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
"""
import math

def sigma(limit):
    result = [1] * limit
    for i in range(2, limit, 2):
        n, a, m, p = i, 1, 1, 2 * 2
        while n % 2 == 0:
            a *= p
            m += a
            n = n // 2
        result[i] *= m
    for i in range(3, limit, 2):
        if result[i] == 1:
            for j in range(i, limit, i):
                n, a, m, p = j, 1, 1, i * i
                while n % i == 0:
                    a *= p
                    m += a
                    n = n // i
                result[j] *= m
    return result

if __name__ == '__main__':
    sieve = sigma(64000000)
    ans = 0
    for n, v in enumerate(sieve):
        sqrt_v = int(math.sqrt(v))
        if sqrt_v ** 2 == v:
            ans += n
    print(ans)
