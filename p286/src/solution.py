'''
Created on Jun 21, 2012

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

def prob(q, n, m):
    # Probability of nailing a single shot at distance x
    s = [1 - decimal.Decimal(x / q) for x in range(n + 1)]
    # Probability of failing a shot at distance x
    f = [decimal.Decimal(x / q) for x in range(n + 1)]
    pascal, row = list(), [1]
    for x in range(1, n + 1):
        p = row[-1] * f[x]
        row.append(p)
    pascal.append(row)
    for i in range(1, m + 1):
        row = [1]
        for x in range(1, i + 1):
            p = row[-1] * s[x]
            row.append(p)
        prow = pascal[-1]
        for x in range(i + 1, n + 1):
            p = row[-1] * f[x] + prow[x - 1] * s[x]
            row.append(p)
        pascal.append(row)
    return pascal[-1][-1]

if __name__ == '__main__':
    q_lb, q_ub, target = 50, 60, decimal.Decimal(0.02)
    ans = 0
    for i in range(40):
        ans = (q_lb + q_ub) / 2
        p = prob(ans, 50, 20)
        if p > target:
            q_lb = ans
        elif p < target:
            q_ub = ans
    print(ans)
