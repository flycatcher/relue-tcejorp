'''
Created on Apr 21, 2012

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
import sys
import math

if __name__ == '__main__':
    words = []
    for line in open(sys.argv[1]):
        for token in line.split(','):
            word = token.strip('"')
            if len(word) > 0:
                words.append(word.lower())
    max_word_length = len(max(words, key=len))
    max_tri_num = math.ceil((math.sqrt(8 * 26 * max_word_length + 1) - 1) / 2)
    triangulars = set([(x * (x + 1)) >> 1 for x in range(1, max_tri_num)])
    offset = ord('a') - 1
    result = 0
    for word in words:
        if sum([ord(ch) - offset for ch in word]) in triangulars:
            result += 1
    print(result)
