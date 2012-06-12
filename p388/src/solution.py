'''
Created on Jun 11, 2012

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

References:

1. http://oeis.org/A090025
2. daniel.is.fischer, http://projecteuler.net/project/resources/073_e5cc8ae355a3
4dab60114be52a61fa27/073_overview.pdf
'''
import math

def lines(m):
    return (m + 1) ** 3 - 1

def distinct_lines(n, small, large, max_m, max_n):
    s = int(math.sqrt(n / 2))
    count = lines(n) - lines(n >> 1)
    m, k = 1, (n - 1) // 2
    while k >= s:
        k_inc = ((n // (m + 1)) - 1) >> 1
        count -= (k - k_inc) * small[m]
        k, m = k_inc, m + 1
    while k > 0:
        m = n // ((k << 1) + 1)
        count -= small[m] if m <= max_m else large[((max_n // m) - 1) >> 1]
        k -= 1
    if n <= max_m:
        small[n] = count
    else:
        large[((max_n // n) - 1) >> 1] = count

if __name__ == '__main__':
    limit = 10 ** 10
    k0 = int(math.sqrt(limit / 2))
    m0 = limit // (2 * k0 + 1)
    dks, dms = [0] * k0, [0] * (m0 + 1)
    for m in range(1, m0 + 1):
        distinct_lines(m, dms, dks, m0, limit)
    for j in range(k0 - 1, -1, -1):
        k = (j << 1) + 1
        distinct_lines(limit // k, dms, dks, m0, limit)
    ans = dks[0]
    print(ans)
