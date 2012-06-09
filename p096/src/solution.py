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
import functools
import sys

def get_zeros(game):
    result = []
    for rdx, row in enumerate(game):
        for cdx, v in enumerate(row):
            if v == 0:
                result.append((rdx, cdx))
    return result

def get_candidates(game, rdx, cdx):
    result = [x for x in range(1, 10)]
    for r, row in enumerate(game):
        for c, v in enumerate(row):
            is_remove = False
            if r == rdx:
                is_remove = True
            elif c == cdx:
                is_remove = True
            elif (r // 3 == rdx // 3) and (c // 3 == cdx // 3):
                is_remove = True
            if is_remove and v in result:
                result.remove(v)
    return result

def solve_game(game):
    result = [x[:] for x in game]
    zeros = get_zeros(result)
    is_reduced = (len(zeros) > 0)
    while is_reduced: # Try to reduce 0s by logical deduction
        is_reduced = False
        for (rdx, cdx) in zeros:
            candidates = get_candidates(result, rdx, cdx)
            if len(candidates) == 1:
                result[rdx][cdx] = candidates[0]
                is_reduced = True
            elif len(candidates) == 0:
                return result # Dead end
        if is_reduced:
            zeros = get_zeros(result)
    if len(zeros) > 0: # Need to start guessing
        (rdx, cdx) = zeros[0]
        candidates = get_candidates(result, rdx, cdx)
        for c in candidates:
            result[rdx][cdx] = c
            tmp = solve_game(result)
            if len(get_zeros(tmp)) == 0:
                result = tmp
                break
    return result

def solve(game):
    g = solve_game(game)
    result = functools.reduce(lambda x, y: 10 * x + y, g[0][:3])
    return result

if __name__ == '__main__':
    games, game = [], []
    for line in open(sys.argv[1]):
        if line.startswith('Grid'):
            game = list()
        else:
            game.append([int(x) for x in line.strip()])
        if len(game) == 9:
            games.append(game)
    ans = sum(map(lambda x: solve(x), games))
    print(ans)
