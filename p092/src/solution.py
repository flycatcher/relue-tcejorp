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
def square_digits(number):
    result = 0
    while number > 0:
        (q, r) = divmod(number, 10)
        result += r ** 2
        number = q
    return result

def count_89ers(number_up_to):
    oners = set([1])
    eighty_niners = set([89])
    result = 0
    
    for x in range(2, (9 ** 9) * len(str(number_up_to))):
        trail = [x]
        while x not in oners and x not in eighty_niners:
            x = square_digits(x)
            trail.append(x)
        if x in oners:
            oners.update(trail)
        else:
            eighty_niners.update(trail)
    for x in range(2, number_up_to):
        if x not in oners and x not in eighty_niners:
            x = square_digits(x)
        if x in eighty_niners:
            result += 1
    return result

if __name__ == '__main__':
    result = count_89ers(10000000)
    print(result)
