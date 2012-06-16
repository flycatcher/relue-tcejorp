'''
Created on Jun 16, 2012

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
import decimal

if __name__ == '__main__':
    n = 1000
    nln2, ln_fac = n * decimal.Decimal(2).ln(), [0] * (n + 1)
    for m in range(1, n + 1):
        ln_fac[m] = ln_fac[m - 1] + decimal.Decimal(m).ln()
    ans = 0
    # Magic number 432 comes from Eq. p(f, k) = (1 + 2f)^k * (1 - f)^(1000 - k).
    # In particular, we want to find a pair of (f, k) such that p(f, k) is
    # greater than or equal to 10^9, where 0 < f < 1, and k is minimized. By
    # equating p(f, k) = 10^9, we have:
    #     k(f) = (9*log(10) - 1000*log(1-f)) / (log(1 + 2*f) - log(1 - f))
    # To minimize k(f), we set d(k)/df = 0 and solve for f, which turns out to
    # be approximately 0.146883922440951. Consequently, the local minimum of
    # k(f) for 0 < f < 1 is 431.25595. We take the next integer.
    for m in range(432, n + 1):
        inc = decimal.Decimal(0)
        inc += ln_fac[-1] - ln_fac[n - m] - ln_fac[m] - nln2
        ans += inc.exp()
    print(ans)
