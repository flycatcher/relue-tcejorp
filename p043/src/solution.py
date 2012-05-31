'''
Created on Apr 22, 2012

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
import functools

def main():
    digits = [x for x in range(0, 10)]
    to_int = lambda x, y: x * 10 + y
    result = 0
    for arrangement in itertools.permutations(digits):
        if arrangement[0] == 0:
            continue
        if functools.reduce(to_int, arrangement[1:4], 0) % 2 != 0:
            continue
        if functools.reduce(to_int, arrangement[2:5], 0) % 3 != 0:
            continue
        if functools.reduce(to_int, arrangement[3:6], 0) % 5 != 0:
            continue
        if functools.reduce(to_int, arrangement[4:7], 0) % 7 != 0:
            continue
        if functools.reduce(to_int, arrangement[5:8], 0) % 11 != 0:
            continue
        if functools.reduce(to_int, arrangement[6:9], 0) % 13 != 0:
            continue
        if functools.reduce(to_int, arrangement[7:10], 0) % 17 != 0:
            continue
        result += functools.reduce(to_int, arrangement, 0)
    return result
    
if __name__ == '__main__':
    print(main())
