'''
Created on Apr 17, 2012

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

if __name__ == '__main__':
    result = 0
    goal = 2000000
    diff = 2000000
    
    for height in range(1, 2001):
        for width in range(2, 2001):
            y = ((height + 1) * height) >> 1
            x = ((width + 1) * width) >> 1
            z = x * y
            if z >= goal:
                if (z - goal) < diff:
                    print('{0}x{1}'.format(height, width))
                    print(z)
                    result = width * height
                    diff = z - goal
                else:
                    x = ((width - 1) * width) >> 1
                    z = x * y
                    if z < goal and (goal - z) < diff:
                        print('{0}x{1}'.format(height, width - 1))
                        print(z)
                        result = height * (width - 1)
                        diff = goal - z
                break
    
    print(result)
