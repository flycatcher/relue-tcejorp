'''
Created on Apr 29, 2012

Copyright (c) 2012 Jun Mei

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
def sieve_totients(upper_bound):
    sieve = [x for x in range(upper_bound)]
    for x in range(2, upper_bound):
        if sieve[x] == x:
            for j in range(x, upper_bound, x):
                sieve[j] -= sieve[j] // x
    return sieve

def is_permutation(x, y):
    str_x, str_y = str(x), str(y)
    if len(str_x) != len(str_y):
        return False
    return sorted(str_x) == sorted(str_y)

if __name__ == '__main__':
    max_number = 10 ** 7
    totients = sieve_totients(max_number)
    result = 0
    min_ratio = max_number
    for i in range(2, max_number):
        totient = totients[i]
        x = i / totient
        if x < min_ratio and is_permutation(totient, i):
            min_ratio = x
            result = i
    print(result)
