'''
Created on Apr 25, 2012

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

def is_palindrome(number):
    if number < 10:
        return True
    str_number = str(number)
    mid_point = len(str_number) >> 1
    for i in range(0, mid_point):
        if str_number[i] != str_number[-(i + 1)]:
            return False
    return True

def reverse(number):
    result = 0
    while number > 0:
        (q, r) = divmod(number, 10)
        result = result * 10 + r
        number = q
    return result

def is_lychrel(number):
    for step in range(0, 50):
        number += reverse(number)
        if is_palindrome(number):
            return False
    return True

def count_lychrels(test_end):
    result = 0
    for x in range(1, test_end):
        if is_lychrel(x):
            result += 1
    return result

if __name__ == '__main__':
    result = count_lychrels(10000)
    print(result)
