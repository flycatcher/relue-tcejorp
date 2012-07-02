'''
Created on Jun 30, 2012

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

1. http://oeis.org/A000213
2. http://mathworld.wolfram.com/TribonacciNumber.html
'''

def is_tribonacci_factor(n):
    t1, t2, t3 = 1, 1, 3
    while (t1, t2, t3) != (1, 1, 1) and t3 > 0:
        t1, t2, t3 = t2, t3, (t1 + t2 + t3) % n
    return (t3 == 0)

if __name__ == '__main__':
    n, ans = 25, list()
    while len(ans) < 124:
        if not is_tribonacci_factor(n):
            ans.append(n)
        n = n + 2
    print(ans[-1])
