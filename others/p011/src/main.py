'''
Created on Sep 8, 2012

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
import random
import string

def count_bits(n):
    result = 0
    while n > 0:
        result += (n & 1)
        n = n >> 1
    return result

def init_bitcount_dict():
    result = dict()
    for ch in string.hexdigits:
        n = int(ch, 16)
        result.setdefault(ch.upper(), count_bits(n))
    return result

def hex_bitcount(text):
    bitcount_dict = init_bitcount_dict()
    result = 0
    for ch in text.upper():
        if ch in bitcount_dict:
            result += bitcount_dict[ch]
        else:
            return -1
    return result

def generate_test():
    x = random.randint(0, 1 << 32)
    text = hex(x)
    ans = count_bits(x)
    return (text[2:], ans)

if __name__ == '__main__':
    tests = []
    tests.append(('2F', count_bits(int('2F', 16))))
    tests.append(('0', count_bits(int('0', 16))))
    tests.append(('1', count_bits(int('1', 16))))
    tests.append(generate_test())
    tests.append(generate_test())
    tests.append(generate_test())
    tests.append(generate_test())
    tests.append(generate_test())
    tests.append(generate_test())
    tests.append(generate_test())
    tests.append(generate_test())
    tests.append(generate_test())
    tests.append(generate_test())
    tests.append(generate_test())
    tests.append(generate_test())
    tests.append(generate_test())
    tests.append(generate_test())
    tests.append(generate_test())
    tests.append(generate_test())
    for (text, expected_result) in tests:
        ans = hex_bitcount(text)
        if not ans == expected_result:
            print('{0}\nExpect={1} Actual={2}'.format(text, expected_result, ans))
        assert ans == expected_result
    print('Tests Passed')
