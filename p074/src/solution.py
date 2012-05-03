'''
Created on May 2, 2012

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
import functools

def factorials(upper_bound):
    result = [1] * upper_bound
    for n in range(2, upper_bound):
        result[n] = result[n - 1] * n
    return result

def get_next(number, mapping):
    result = 0 if number > 0 else 1
    while number > 0:
        (number, r) = divmod(number, 10)
        result += mapping[r]
    return result

def count_chains(upper_bound, chain_size):
    fact_table = factorials(10)
    chain_lengths = [0] * upper_bound
    # Known loops: 169 => 363601 => 1454 => 169 
    for x in [169, 363601, 1454]:
        if upper_bound > x:
            chain_lengths[x] = 3
    # Known loops: 871 => 45361 => 871 and 872 => 45362 => 872 
    for x in [871, 45361, 872, 45362]:
        if upper_bound > x:
            chain_lengths[x] = 2
    for x in range(1, upper_bound):
        if chain_lengths[x] > 0:
            continue
        chain = [x]
        chain_set = set(chain)
        while True:
            size = len(chain)
            x_last = chain[size - 1]
            x_next = get_next(x_last, fact_table)
            if x_next < upper_bound and chain_lengths[x_next] > 0:
                base_length = chain_lengths[x_next]
                for idx, num in enumerate(chain):
                    if num < upper_bound:
                        chain_lengths[num] = base_length + size - idx
                break
            if x_next in chain_set:
                position = chain.index(x_next)
                for idx, num in enumerate(chain[0:position]):
                    if num < upper_bound:
                        chain_lengths[num] = size - idx
                loop_size = size - position
                for num in chain[position:]:
                    if num < upper_bound:
                        chain_lengths[num] = loop_size
                break
            chain.append(x_next)
            chain_set.add(x_next)
    result = functools.reduce(lambda x, y: (x + 1) if y == chain_size else x, chain_lengths[1:], 0)
    return result

if __name__ == '__main__':
    result = count_chains(1000000, 60)
    print(result)
