'''
Created on Jun 10, 2012

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

1. http://en.wikipedia.org/wiki/De_Bruijn_sequence
2. http://en.wikipedia.org/wiki/Linear_feedback_shift_register
3. http://en.wikipedia.org/wiki/Gray_code
'''
import copy
import functools

def rings(unvisited, visited, width):
    w = 2 ** width
    if len(unvisited) < width:
        o = (visited[-1] << 1) % w
        while o > 0:
            if o not in unvisited:
                return [] # Dead end
            unvisited.remove(o)
            o = (o << 1) % w
        if len(unvisited) > 0:
            return []
        else:
            return [visited]
    result = []
    o = (visited[-1] << 1) % w
    if o in unvisited:
        u = copy.copy(unvisited)
        u.remove(o)
        v = copy.copy(visited)
        v.append(o)
        result = result + rings(u, v, width)
    o = (o + 1) % w
    if o in unvisited:
        u = copy.copy(unvisited)
        u.remove(o)
        v = copy.copy(visited)
        v.append(o)
        result = result + rings(u, v, width)
    return result

def to_int(circle):
    ans = functools.reduce(lambda x, y: (x << 1) + (y & 1), circle[1:])
    return ans

if __name__ == '__main__':
    bits = 5
    codes = set(x for x in range(2, 2 ** bits))
    circles = rings(codes, [0, 1], bits)
    ans = sum(to_int(x) for x in circles)
    print(ans)
