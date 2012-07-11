'''
Created on Jul 10, 2012

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

1. http://www.360doc.com/content/06/0104/10/2311_53610.shtml
2. http://stackoverflow.com/questions/4214114/suggest-an-efficient-
algorithm/4215034#4215034
'''
import math

def equivalent_games(n):
    """
    Creates a mapping for a n-value Nim-Square game to a Nim game
    """
    result = [0] * n
    for b in range(1, n):
        sqrt_k = int(math.sqrt(b))
        remainders = set(result[b - r ** 2] for r in range(1, sqrt_k + 1))
        for a in range(b + 1):
            if a not in remainders:
                result[b] = a
                break
    return result

if __name__ == '__main__':
    n = 1 + (10 ** 5)
    nim = equivalent_games(n)
    max_nim, ans = max(nim), 0
    freq = [0] * (max_nim + 1)
    counts = [0] * (max_nim + 1)
    for a in nim:
        freq[a] += 1
        # In each iteration i, counts keeps track of the number of unordered
        # tuples (a, b), where a <= b <= i, such that (a, b, i) forms a losing
        # position for the starting player.
        for b, v in enumerate(freq):
            # a ^ b ^ c == 0 <=> a ^ b == c; if c is a valid Nim number, we need
            # to update the partial count of Nim-Square games with losing
            # positions for the starting player for the current iteration i with
            # respect to the equivalent Nim game with value c.
            if (a ^ b) <= max_nim:
                counts[a ^ b] += v
        ans += counts[a]
    print(ans)
