'''
Created on Jun 9, 2012

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
import math

def cuboids(m):
    result, m_sq = 0, m ** 2
    for ab in range(3, (m << 1) + 1):
        c_sq = ab ** 2 + m_sq
        c = int(math.sqrt(c_sq))
        if c ** 2 == c_sq:
            result += (ab >> 1) if ab <= m else m - ((ab - 1) >> 1)
    return result

if __name__ == '__main__':
    ans, count, threshold = 1, 0, 10 ** 6
    while count < threshold:
        ans += 1
        count += cuboids(ans)
    print(ans)
