'''
Created on Jun 6, 2012

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

if __name__ == '__main__':
    limit = 51
    # Array @reds is a container for the number of configurations with red color
    # tiles; the index value is the full length of the tile row. Clearly, for
    # length 0 and 1, the number of configurations is zero because each red tile
    # takes 2 spaces.
    reds = [0, 0]
    while len(reds) < limit:
        e = len(reds) - 1
        reds.append(sum(reds[:e]) + e)
    # Each green tile takes 3 spaces
    greens = [0, 0, 0]
    while len(greens) < limit:
        e = len(greens) - 2
        greens.append(sum(greens[:e]) + e)
    # Each blue tile takes 4 spaces
    blues = [0, 0, 0, 0]
    while len(blues) < limit:
        e = len(blues) - 3
        blues.append(sum(blues[:e]) + e)
    ans = reds[-1] + greens[-1] + blues[-1]
    print(ans)
