'''
Created on Apr 20, 2012

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

if __name__ == '__main__':
    triangles = []
    for line in open(sys.argv[1]):
        line = line.strip()
        if len(line) > 0:
            coordinates = [int(x) for x in line.split(',', 5)]
            triangles.append(coordinates)
    result = 0
    # Let v1, v2, v3 be the three vertices of a triangle, and p be any point in
    # the same plane. There must exist scalar values a and b, such that
    #     p = v1 + a * (v2 - v1) + b * (v3 - v1)
    # If a and b are both greater than 0, and a + b < 1, then p lies strictly
    # within the triangle.
    for [x1, y1, x2, y2, x3, y3] in triangles:
        det = (x2 - x1) * (y3 - y1) - (x3 - x1) * (y2 - y1)
        if det == 0:
            continue
        detA = (x3 - x1) * y1 - x1 * (y3 - y1)
        detB = x1 * (y2 - y1) - (x2 - x1) * y1
        a = detA / det
        b = detB / det
        if a > 0 and b > 0 and (a + b) < 1:
            result += 1    
    print(result)
