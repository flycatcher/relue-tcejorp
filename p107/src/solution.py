'''
Created on Jun 12, 2012

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

References:

1. http://en.wikipedia.org/wiki/Minimum_spanning_tree
2. http://en.wikipedia.org/wiki/Prim%27s_algorithm
'''
import sys
import heapq

if __name__ == '__main__':
    weights, node = dict(), 0
    for line in open(sys.argv[1]):
        for idx, s in enumerate(line.strip().split(',')):
            if s.isdigit():
                weights.setdefault('{0},{1}'.format(node, idx), int(s))
        node += 1
    min_weights = [float('inf')] * node
    min_weights[0] = 0
    queue = [[w, n] for n, w in enumerate(min_weights)]
    while queue:
        heapq.heapify(queue)
        [w, n] = heapq.heappop(queue)
        for v in queue:
            u = v[1]
            k = '{0},{1}'.format(n, u)
            if k in weights and weights[k] < min_weights[u]:
                min_weights[u], v[0] = weights[k], weights[k]
    ans = (sum(weights.values()) >> 1) - sum(min_weights)
    print(ans)
