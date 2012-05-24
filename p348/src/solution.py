'''
Created on May 23, 2012

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
import functools

squares = set(x ** 2 for x in range(2, 10 ** 5))
cubes = [x ** 3 for x in range(2, 32 ** 3)]

def count_ways(x):
    result = 0
    for cube in cubes:
        r = x - cube
        if r < 0:
            break
        elif r in squares:
            result += 1
    return result

def palindromes(x):
    digits = []
    while x > 0:
        (q, r) = divmod(x, 10)
        digits.append(r)
        x = q
    d1 = digits[1:]
    d1.reverse()
    d1.extend(digits)
    p1 = functools.reduce(lambda x, y: x * 10 + y, d1)
    d2 = digits[:]
    d2.reverse()
    d2.extend(digits)
    p2 = functools.reduce(lambda x, y: x * 10 + y, d2)
    return (p1, p2)

if __name__ == '__main__':
    ans = 0
    count = 5
    prefix = 100
    while count > 0:
        (p1, p2) = palindromes(prefix)
        if count_ways(p1) == 4:
            print(p1)
            ans += p1
            count -= 1
        if count_ways(p2) == 4:
            print(p2)
            ans += p2
            count -= 1
        prefix += 1
    print(ans)
