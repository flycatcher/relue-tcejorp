'''
Created on Jun 24, 2012

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

if __name__ == '__main__':
    # Array nt holds the expected number of plates that we need to encounter
    # before seeing the first pair of numbers that add up to 1000, assuming that
    # we have already seen XYZ-500. The index indicates the total number of
    # distinct numbers we have seen so far. Array nf is similar to nt except
    # that nf assumes we haven't seen XYZ-500 yet.
    nt, nf = [0] * 500, [0] * 500
    nt[499] = 2
    nf[499] = 2 + nt[499] / 500
    for n in range(498, -1, -1):
        scale, remainder = 1000 / (999 - n), 1000 - 2 * (n + 1)
        nt[n] = scale * (1 + remainder * nt[n + 1] / 1000)
        nf[n] = scale * (1 + nt[n] / 1000 + remainder * nf[n + 1] / 1000)
    print('{0:.8f}'.format(nf[0]))
