'''
Created on Jun 27, 2012

Copyright (C) 2012, Jun Mei

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
import functools
import itertools
import sys

def special_sum(numbers):
    is_valid = True
    last_stage = set()
    for x in numbers:
        if x in last_stage:
            is_valid = False
            break
        last_stage.add(x)
    size, max_size = 2, (len(numbers) >> 1) + 2
    while is_valid and size < max_size:
        current_stage = set()
        for c in itertools.combinations(numbers, r=size):
            s = sum(c)
            if s in current_stage:
                is_valid = False
                break
            current_stage.add(s)
        if min(current_stage) <= max(last_stage):
            is_valid = False
        last_stage, size = current_stage, size + 1
    return sum(numbers) if is_valid else 0

if __name__ == '__main__':
    input_sets = []
    for line in open(sys.argv[1]):
        s = list()
        for token in line.strip().split(','):
            if token.isdigit():
                s.append(int(token))
        input_sets.append(s)
    ans = functools.reduce(lambda x, y: x + special_sum(y), input_sets, 0)
    print(ans)
