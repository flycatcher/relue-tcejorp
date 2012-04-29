'''
Created on Apr 27, 2012

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
import itertools

def sieve_primes(max_number):
    sieve = [True] * max_number
    for i in range(2, max_number):
        if sieve[i]:
            for j in range(i << 1, max_number, i):
                sieve[j] = False
    return [x for x in range(2, max_number) if sieve[x]]

def get_masks(x, min_sim):
    digit_counts = {}
    str_x = str(x)
    for digit in str_x:
        digit_counts.setdefault(digit, 0)
        digit_counts[digit] += 1
    result = []
    for digit in digit_counts:
        if digit_counts[digit] < min_sim:
            continue
        indices = [i for i, c in enumerate(str_x) if c == digit]
        for position in itertools.combinations(indices, min_sim):
            letters = [v if i not in position else 'x' for i, v in enumerate(str_x)]
            result.append(''.join(letters))
    return result

def list_family(max_number, min_sim, min_size):
    primes = sieve_primes(max_number)
    mask_counts = {}
    for p in primes:
        masks = get_masks(p, min_sim)
        if len(masks) == 0:
            continue
        for mask in masks:
            mask_counts.setdefault(mask, list())
            mask_counts[mask].append(p)
    for mask in mask_counts:
        counts = mask_counts[mask]
        if len(counts) >= min_size:
            print(counts)

if __name__ == '__main__':
    list_family(1000000, 3, 8)
