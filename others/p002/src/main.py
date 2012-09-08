'''
Created on Sep 7, 2012

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
'''
def max_binary_ones_stretch(n):
    while n > 0 and (n & 1) == 0:
        n = n >> 1
    result, stretch = 0, 0
    while n > 0:
        stretch = stretch + 1 if (n & 1) == 1 else 0
        if stretch > result:
            result = stretch
        n = n >> 1
    return result

if __name__ == '__main__':
    tests = []
    tests.append((int('0b11011110110010011', 2), 4))
    tests.append((int('0b100000001', 2), 1))
    tests.append((int('0b11000000000000000000000', 2), 2))
    tests.append((int('0b111111000011111000111111', 2), 6))
    tests.append((int('0b0', 2), 0))
    for (n, expected_result) in tests:
        result = max_binary_ones_stretch(n)
        assert result == expected_result
    print('Tests Passed')
