'''
Created on Jun 30, 2012

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

def not_bouncy_numbers(e):
    inc_counts = [1] * 10
    dp_inc_counts = [inc_counts]
    for k in range(e):
        inc_counts, last_inc_counts = [1], dp_inc_counts[-1]
        for n in range(1, 10):
            x = inc_counts[-1] + last_inc_counts[n]
            inc_counts.append(x)
        dp_inc_counts.append(inc_counts)
    dec_counts = [1] * 10
    dp_dec_counts = [dec_counts]
    for k in range(e):
        dec_counts, last_dec_counts = [1] * 10, dp_dec_counts[-1]
        for n in range(8, 0, -1):
            dec_counts[n] = dec_counts[n + 1] + last_dec_counts[n]
        dp_dec_counts.append(dec_counts)
    result = 0
    for c in dp_inc_counts:
        result += sum(c[1:])
    for c in dp_dec_counts:
        result += sum(c[1:])
    result -= 9 * (e + 1)
    return result

if __name__ == '__main__':
    ans = not_bouncy_numbers(99)
    print(ans)
