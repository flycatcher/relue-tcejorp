'''
Created on Jun 9, 2012

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

1. Jakub Pawlewicz and Mihai Patrascu, Order Statistics in the Farey Sequences
in Sublinear Time and Counting Primitive Lattice Points in Polygons,
http://people.csail.mit.edu/mip/papers/farey2/paper.ps

2. Hiroki Yanagisawa, A Simple Algorithm for Lattice Point Counting in Rational
Polygons, http://domino.research.ibm.com/library/cyberdig.nsf/1e4115aea78b6e7c85
256b360066f0d4/998d6b527637a012852572730025e777?OpenDocument&Highlight=0,a
'''

def binary_search(m, s):
    """
    Find the smallest n such that floor(m / n) < s
    """
    if s <= 1:
        return m + 1
    upper, lower = m, 2
    while True:
        n = (upper + lower) >> 1
        t = m // n
        if t < s and m // (n - 1) == s:
            return n
        elif t >= s:
            lower = n
        elif t <= s - 1:
            upper = n

def primitives(p, sp):
    """
    Calculates the number of primitive lattices enclosed within a right triangle
    defined by (0, 0), (p, 0) and (0, p)
    """
    if p in sp:
        return sp[p]
    result = (p * (p + 1)) >> 1
    d = 2
    while d <= p:
        s = p // d
        dn = binary_search(p, s)
        result -= primitives(s, sp) * (dn - d)
        d = dn
    sp.setdefault(p, result)
    return result

if __name__ == '__main__':
    sp, size = dict(), 10 ** 8
    sp.setdefault(1, 1)
    ans = ((size * (size + 1) >> 1) - primitives(size, sp)) * 6
    print(ans)
