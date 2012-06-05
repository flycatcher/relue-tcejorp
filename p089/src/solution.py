'''
Created on Jun 2, 2012

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
import sys

def int_to_roman(n):
    result = []
    while n >= 1000:
        result.append('M')
        n -= 1000
    if n >= 900:
        result.append('CM')
        n -= 900
    if n >= 500:
        result.append('D')
        n -= 500
    if n >= 400:
        result.append('CD')
        n -= 400
    while n >= 100:
        result.append('C')
        n -= 100
    if n >= 90:
        result.append('XC')
        n -= 90
    if n >= 50:
        result.append('L')
        n -= 50
    if n >= 40:
        result.append('XL')
        n -= 40
    while n >= 10:
        result.append('X')
        n -= 10
    if n >= 9:
        result.append('IX')
        n -= 9
    if n >= 5:
        result.append('V')
        n -= 5
    if n >= 4:
        result.append('IV')
        n -= 4
    while n >= 1:
        result.append('I')
        n -= 1
    return ''.join(result);

def roman_to_int(s):
    m = {}
    m['I'] = 1
    m['V'] = 5
    m['X'] = 10
    m['L'] = 50
    m['C'] = 100
    m['D'] = 500
    m['M'] = 1000
    result = 0
    p = ''
    for c in s[::-1]:
        if c == 'C' and (p == 'D' or p == 'M'):
            result -= m[c]
        elif c == 'X' and (p == 'L' or p == 'C'):
            result -= m[c]
        elif c == 'I' and (p == 'V' or p == 'X'):
            result -= m[c]
        else:
            result += m[c]
        p = c
    return result

if __name__ == '__main__':
    romans = []
    for line in open(sys.argv[1]):
        line_clean = line.strip().upper()
        if len(line_clean) == 0:
            continue
        romans.append(line_clean)
    ans = 0
    for s in romans:
        n = roman_to_int(s)
        m = int_to_roman(n)
        print(s, n, m)
        ans += len(s) - len(m)
    print(ans)
