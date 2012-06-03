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
import fractions
import itertools

def count_triangles(size):
    result = size ** 2;
    for (x, y) in itertools.product(range(size + 1), repeat=2):
        f = fractions.gcd(x, y)
        if f == 0: # Skip the origin
            continue
        s_x, s_y = y // f, -x // f
        xp, yp = x - s_x, y - s_y
        while xp >= 0 and xp <= size and yp >= 0 and yp <= size:
            result += 1
            xp -= s_x
            yp -= s_y
        xp, yp = x + s_x, y + s_y
        while xp >= 0 and xp <= size and yp >= 0 and yp <= size:
            result += 1
            xp += s_x
            yp += s_y
    return result

if __name__ == '__main__':
    ans = count_triangles(50)
    print(ans)
