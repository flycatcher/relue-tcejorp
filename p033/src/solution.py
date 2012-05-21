'''
Created on Apr 19, 2012

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
    digits = [i for i in range(1, 10)]
    for a in digits:
        for (b, c) in itertools.combinations(digits, 2):
            # case 1 ab/ac = b/c
            left = (a * 10 + b) * c
            right = (a * 10 + c) * b
            if left == right:
                print('{0}{1}/{0}{2}'.format(a, b, c))
            # case 2 ba/ac = b/c
            left = (b * 10 + a) * c
            right = (a * 10 + c) * b
            if left == right:
                print('{1}{0}/{0}{2}'.format(a, b, c))
            # case 3 ab/ca = b/c
            left = (a * 10 + b) * c
            right = (c * 10 + a) * b
            if left == right:
                print('{0}{1}/{2}{1}'.format(a, b, c))
            # case 4 ba/ca = b /c
            left = (b * 10 + a) * c
            right = (c * 10 + a) * b
            if left == right:
                print('{1}{0}/{2}{1}'.format(a, b, c))
