'''
Created on Jun 4, 2012

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
import decimal

def fx(r):
    a = 1 - r
    result = 900 * (1 - r ** 5000) / a
    result += 3 * 5001 * (r ** 5000) / a
    result -= 3 * (1 - r ** 5001) / (a ** 2)
    return result

if __name__ == '__main__':
    decimal.getcontext().prec = 18
    x_min = decimal.Decimal(1)
    x_max = decimal.Decimal(2)
    x = (x_min + x_max) / 2
    y_zero = decimal.Decimal(-600000000000)
    y = fx(x)
    while abs(y - y_zero) > 0.1:
        y = fx(x)
        if y > y_zero:
            x_min = x
        elif y < y_zero:
            x_max = x
        x = (x_min + x_max) / 2
    print(x)
