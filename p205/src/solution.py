'''
Created on May 11, 2012

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

def prob():
    pyramidal = [x for x in range(1, 5)]
    cubic = [x for x in range(1, 7)]
    num_pyramial, num_cubic = 9, 6
    pyramial_totals = [0] * (4 * num_pyramial + 1)
    cubic_totals = [0] * (6 * num_cubic + 1)
    for roll in itertools.product(pyramidal, repeat=num_pyramial):
        total = sum(roll)
        pyramial_totals[total] += 1
    for roll in itertools.product(cubic, repeat=num_cubic):
        total = sum(roll)
        cubic_totals[total] += 1
    num_pyramial_wins = 0
    for py_total, py_count in enumerate(pyramial_totals):
        cu_total = sum(cubic_totals[0:py_total])
        num_pyramial_wins += py_count * cu_total
    num_rolls = sum(pyramial_totals) * sum(cubic_totals)
    result = num_pyramial_wins / num_rolls
    return result

if __name__ == '__main__':
    ans = prob()
    print(ans)
