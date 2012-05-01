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
import sys

def main(number):
    sieve = [0] * number
    for x in range(2, number):
        if sieve[x] == 0:
            for y in range(2 * x, number, x):
                sieve[y] += 1
    result = 210 # = 2 x 3 x 5 x 7
    while result < number - 4:
        if sieve[result + 3] < 4:
            result += 4
        elif sieve[result + 2] < 4:
            result += 3
        elif sieve[result + 1] < 4:
            result += 2
        elif sieve[result] < 4:
            result += 1
        else:
            print(result)
            sys.exit(0)
    print('not found :(')

if __name__ == '__main__':
    main(150000)
