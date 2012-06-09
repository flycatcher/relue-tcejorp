'''
Created on Jun 8, 2012

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
import itertools

if __name__ == '__main__':
    ans, max_length = (), 0
    for (a, b, c, d) in itertools.combinations(range(1, 10), r=4):
        n = set()
        for (x1, x2, x3, x4) in itertools.permutations([a, b, c, d]):
            for (op1, op2, op3) in itertools.product(['+', '-', '*', '/'], repeat=3):
                try:
                    s = '(({0}{1}{2}){3}{4}){5}{6}'.format(x1, op1, x2, op2, x3, op3, x4)
                    x = eval(s)
                    if x > 0 and int(x) == x:
                        n.add(int(x))
                except ZeroDivisionError:
                    pass
                try:
                    s = '({0}{1}{2}){3}({4}{5}{6})'.format(x1, op1, x2, op2, x3, op3, x4)
                    x = eval(s)
                    if x > 0 and int(x) == x:
                        n.add(int(x))
                except ZeroDivisionError:
                    pass
        m = 0
        for i, v in enumerate(sorted(n)):
            if i != v - 1:
                break
            m += 1
        if m > max_length:
            ans = (a, b, c, d)
            max_length = m
    print(ans)
