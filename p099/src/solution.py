'''
Created on Apr 28, 2012

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
from math import log10
import sys

def get_max(base_exp_pairs):
    result, max_log = 0, 0
    for i, (base, exp) in enumerate(base_exp_pairs):
        x = exp * log10(base)
        if x > max_log:
            max_log = x
            result = i + 1
    return result

if __name__ == '__main__':
    base_exp_pairs = []
    for line in open(sys.argv[1]):
        clean_line = line.strip()
        if len(clean_line) == 0:
            continue
        tokens = clean_line.split(',')
        if len(tokens) == 2:
            base_exp_pairs.append((int(tokens[0]), int(tokens[1])))
    result = get_max(base_exp_pairs)
    print(result)
