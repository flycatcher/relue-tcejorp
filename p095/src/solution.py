'''
Created on May 27, 2012

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

1. http://mathworld.wolfram.com/DivisorFunction.html
2. http://mathworld.wolfram.com/RestrictedDivisorFunction.html
3. http://mathworld.wolfram.com/SociableNumbers.html
'''
def rdf(limit):
    """
    Returns the sum of all proper (aliquot) divisors for each integer up to the
    given upper bound (exclusive) 
    """
    sieve = [1] * limit
    sieve[0] = 0
    for n in range(2, limit, 2):
        x = 1
        (q, r) = divmod(n, 2)
        while r == 0:
            x += 1
            (q, r) = divmod(q, 2)
        sieve[n] *= (2 ** x - 1)
    for n in range(3, limit, 2):
        if sieve[n] == 1:
            d = n - 1
            for m in range(n, limit, n):
                x = 1
                (q, r) = divmod(m, n)
                while r == 0:
                    x += 1
                    (q, r) = divmod(q, n)
                sieve[m] *= (n ** x - 1) // d
    for n in range(limit):
        sieve[n] -= n
    return sieve

if __name__ == '__main__':
    limit = 10 ** 6
    rdf_map = rdf(limit)
    # Aliquot sequence for each natural number. If the value is greater than 0,
    # it's a social number, and the value is the rank (chain period); if the
    # value is -1, it means the sequence leads to a perfect number; if the value
    # is -2, it means the sequence leads to a prime; if the value is -3, it
    # means the sequence leads to a set of social numbers; if the value is -4,
    # it means some element in the sequence is out of bound.
    aliquot_seq = [0] * limit
    for n in range(2, limit):
        x = rdf_map[n]
        if x == n:
            aliquot_seq[n] = -1
        elif x == 1:
            aliquot_seq[n] = -2
        elif x >= limit:
            aliquot_seq[n] = -4
        elif aliquot_seq[x] > 0:
            aliquot_seq[n] = -3
        else:
            visited = set()
            visited.add(n)
            while x not in visited:
                visited.add(x)
                x = rdf_map[x]
                if x == n:
                    aliquot_seq[n] = len(visited)
                    break
                elif x == 1:
                    aliquot_seq[n] = -2
                    break
                elif x >= limit:
                    aliquot_seq[n] = -4
                    break
                elif aliquot_seq[x] > 0:
                    aliquot_seq[n] = -3
                    break
    for n, r in enumerate(aliquot_seq):
        if r > 0:
            print('{0} rank {1}'.format(n, r))
