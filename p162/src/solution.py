'''
Created on Jun 29, 2012

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

1. http://en.wikipedia.org/wiki/Inclusion%E2%80%93exclusion_principle
'''

def count(n):
    """
    Returns the number of hexadecimal numbers with at most n digits where each
    number contains at least one 0, one 1, and one A
    """
    result, a, b, c = 16 ** n, 15 ** n, 14 ** n, 13 ** n
    result -= (2 * a + 15 * (a - 1) // 14)
    result += b + 2 * 14 * (b - 1) // 13
    result -= 13 * (c - 1) // 12
    return result

if __name__ == '__main__':
    ans = count(16)
    ans = (hex(ans)[2:]).upper()
    print(ans)
