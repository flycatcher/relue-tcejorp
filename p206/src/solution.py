'''
Created on May 10, 2012

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
from queue import Queue
import functools

def to_int(lst):
    return functools.reduce(lambda x, y: x * 10 + y, lst, 0)

def verify_parts(x):
    digits = [str(x) for x in range(9, 0, -1)]
    digits.insert(0, '0')
    y = []
    y.extend(x)
    if x[0] == 0:
        y.insert(0, 1)
    x_sq = to_int(y) ** 2
    str_x_sq = str(x_sq)
    size = len(x)
    for i in range(0, size, 2):
        if str_x_sq[-i - 1] != digits[i // 2]:
            return False
    return True

def successors(x):
    result = []
    if len(x) < 10:
        for a in range(10):
            lst = [a]
            lst.extend(x)
            if verify_parts(lst):
                result.append(lst)
    return result

def verify(x):
    x_sq = to_int(x) ** 2
    digits = []
    while x_sq > 0:
        (q, r) = divmod(x_sq, 10)
        digits.insert(0, r)
        x_sq = q
    if len(digits) != 19:
        return False
    for n in range(1, 10):
        if digits[2 * (n - 1)] != n:
            return False
    return True

def bfs():
    frontier = Queue()
    frontier.put([0])
    while frontier.qsize() > 0:
        candidate = frontier.get()
        if verify(candidate):
            print(to_int(candidate))
            break
        for x in successors(candidate):
            frontier.put(x)

if __name__ == '__main__':
    bfs()
