'''
Created on May 5, 2012

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
import itertools
import re

def to_int(tup):
    result = functools.reduce(lambda x, y: x * 10 + y, tup, 0)
    return result

pattern_9s = re.compile('^(9+)(0*)$')

def special_case(x):
    result = 0
    m = pattern_9s.match(str(x))
    if m != None:
        x = []
        n = len(m.group(1))
        for d in range(1, 9, 2):
            x.extend([d] * n)
        result = to_int(x) + 1
    return result

def least_multiplier(x):
    mod_map = {}
    num_digits, result = 0, special_case(x)
    while result == 0:
        m, offset = 0, 10 ** num_digits
        for digits in itertools.product([0, 1], repeat=num_digits):
            n = offset + to_int(digits)
            r = n % x
            mod_map.setdefault(r, n)
            if mod_map[r] > n:
                mod_map[r] = n
        num_digits += 1
        if 0 in mod_map:
            m = mod_map[0]
        mod_0s = []
        for i in mod_map.keys():
            if (x - i) in mod_map:
                mod_0s.append(mod_map[i] + mod_map[x - i])
        if len(mod_0s) > 0:
            min_mod_0 = min(mod_0s)
            if m == 0 or min_mod_0 < m:
                m = min_mod_0
        if m > 0:
            result = m // x
    return result

if __name__ == '__main__':
    ans = 0
    for x in range(1, 10001):
        ans += least_multiplier(x)
    print(ans)
