'''
Created on Jun 22, 2012

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

1. http://mathworld.wolfram.com/ZeckendorfRepresentation.html
2. http://oeis.org/A014417
3. http://oeis.org/A007895
4. http://oeis.org/A179180
'''
import functools

def zeckendorf_sums(limit):
    result = [(1, 1), (1, 1)]
    total = functools.reduce(lambda x, y: x + y[0], result, 0)
    while total < limit:
        p1, p2 = result[-1], result[-2]
        next_total, next_sum = p1[0] + p2[0], p1[1] + p2[0] + p2[1]
        total += next_total
        result.append((next_total, next_sum))
    return result

def partial_sums(n, partials):
    result, k = 0, 0
    if n == 0:
        return result
    for i, (m, s) in enumerate(partials):
        if m == n:
            return s
        if m > n:
            k = i - 1
            break
    (m, s) = partials[k]
    result += s + (n - m) + partial_sums(n - m, partials)
    return result

def full_sums(n, partials):
    result, total = 0, 0
    for (m, s) in partials:
        if total + m > n:
            break
        total, result = total + m, result + s
    result += partial_sums(n - total, partials)
    return result

if __name__ == '__main__':
    target = (10 ** 17) - 1
    zeckendorf_partials = zeckendorf_sums(target)
    ans = full_sums(target, zeckendorf_partials)
    print(ans)
