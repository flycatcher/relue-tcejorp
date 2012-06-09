'''
Created on Jun 8, 2012

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

if __name__ == '__main__':
    faces = [str(x) for x in range(10)]
    sq = set(['01', '04', '09', '16', '25', '36', '49', '64', '81'])
    ans = set()
    for c1 in itertools.combinations(faces, r=6):
        c1_s = ''.join(c1)
        c1_set = set(c1)
        if '6' in c1_set:
            c1_set.add('9')
        elif '9' in c1_set:
            c1_set.add('6')
        for c2 in itertools.combinations(faces, r=6):
            c2_set = set(c2)
            if '6' in c2_set:
                c2_set.add('9')
            elif '9' in c2_set:
                c2_set.add('6')
            j = set()
            for (a1, a2) in itertools.product(c1_set, c2_set):
                j.add(a1 + a2)
                j.add(a2 + a1)
            if sq <= j:
                c2_s = ''.join(c2)
                p = sorted([c1_s, c2_s])
                ans.add(','.join(p))
    print(len(ans))

