'''
Created on Jun 15, 2012

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

References:

1. http://mathforum.org/library/drmath/view/56650.html
'''
import decimal

if __name__ == '__main__':
    k, n, f = 20000, 1000000, 0
    facts = [0] * (n + 1)
    for p in range(1, n + 1):
        f = f + decimal.Decimal(p).ln()
        facts[p] = f
    ln2, kLnN, ans = decimal.Decimal(2).ln(), k * decimal.Decimal(n).ln(), 0
    for m in range((k >> 1) + 1):
        inc = decimal.Decimal(0)
        inc += facts[n] - facts[n - m] - facts[m]
        inc += facts[k] - facts[k - 2 * m]
        inc += facts[n - m] - facts[n + m - k]
        inc -= (m * ln2 + kLnN)
        ans += inc.exp()
    print(1 - ans)
