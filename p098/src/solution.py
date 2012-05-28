'''
Created on May 27, 2012

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
import math
import sys

def pattern(s):
    letters = [c for c in s]
    letters.sort()
    return (''.join(letters), s)

def pattern_sq(n):
    sq = str(n ** 2)
    return pattern(sq)

def sub_pattern(word, pattern):
    result = map(lambda x: pattern[x] if x in pattern else 'x', word)
    return ''.join(result)

def match_pattern(word, sq):
    result = {}
    for (c, d) in zip(word, sq):
        result[c] = d
    for (c1, c2) in itertools.combinations(result.keys(), r=2):
        if result[c1] == result[c2]:
            result[c2] = 'x'
    return result

sq_anagrams_map = {}

def sq_anagrams(size):
    if size in sq_anagrams_map:
        return sq_anagrams_map[size]
    n_anagrams = {}
    l = math.ceil((math.sqrt(10 ** (size - 1))))
    u = math.ceil((math.sqrt(10 ** size)))
    for (p, s) in map(pattern_sq, range(l, u)):
        n_anagrams.setdefault(p, [])
        n_anagrams[p].append(s)
    for p in [p for (p, s) in n_anagrams.items() if len(s) == 1]:
        del n_anagrams[p]
    sq_anagrams_map[size] = sorted(n_anagrams.values(), key=max, reverse=True)
    return sq_anagrams_map[size]

def sq_match(words):
    n_anagrams = sq_anagrams(len(words[0]))
    result = 0
    for (w1, w2) in itertools.combinations(words, r=2):
        for sq_lst in n_anagrams:
            if int(max(sq_lst)) < result:
                break
            for sq in sq_lst:
                p = match_pattern(w1, sq)
                n = sub_pattern(w2, p)
                if n != sq and n in sq_lst and max(int(sq), int(n)) > result:
                    print('{0} <= {1}, {2} <= {3}'.format(w1, sq, w2, n))
                    result = max(int(sq), int(n))
    return result

if __name__ == '__main__':
    words = []
    if len(sys.argv) > 1:
        for l in open(sys.argv[1]):
            words.extend(s.strip().strip('"').lower() for s in l.split(','))
    w_anagrams = {}
    for (p, s) in map(pattern, words):
        w_anagrams.setdefault(p, [])
        w_anagrams[p].append(s)
    for p in [p for (p, s) in w_anagrams.items() if len(s) == 1]:
        del w_anagrams[p]
    ans = 0
    size = 0
    for p in sorted(w_anagrams.keys(), key=len, reverse=True):
        if len(p) < size:
            break
        sq = sq_match(w_anagrams[p])
        if sq > ans:
            ans = sq
            size = len(p)
    print(ans)
