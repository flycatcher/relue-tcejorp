'''
Created on Jun 3, 2012

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

def sieve_factors(limit):
    result = []
    for x in range(limit):
        result.append([])
    for x in range(2, limit):
        for y in range(x << 1, limit, x):
            result[y].append(x)
    return result

def factorize(n, factors):
    if n <= 1:
        return []
    result = []
    for f in factors:
        (q, r) = divmod(n, f)
        if r == 0:
            sf = factorize(q, factors)
            if len(sf) == 0:
                result.append([f])
            for subfactors in sf:
                b = sorted([f] + subfactors)
                if b not in result:
                    result.append(b)
    return result

if __name__ == '__main__':
    limit = 12000
    factors = sieve_factors(limit * 2 + 1)
    sizes = set()
    unmatch = set(x for x in range(2, limit + 1))
    for n, fs in enumerate(factors):
        if len(unmatch) == 0:
            break
        if len(fs) < 1:
            continue
        for m in factorize(n, fs):
            k = len(m) + n - sum(m)
            if k in unmatch:
                sizes.add(n)
                unmatch.remove(k)
    ans = sum(sizes)
    print(ans)
