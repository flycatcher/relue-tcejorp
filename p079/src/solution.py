'''
Created on Apr 15, 2012

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
import queue
import sys

if __name__ == '__main__':
    clues = []
    
    for line in open(sys.argv[1]):
        s = line.strip()
        if len(s) > 0:
            clues.append(s) 
    
    freq = {}
    result = []
    
    while len(clues) > 0:
        # For the next set of available clues, get the leading digit from each
        # clue and do a frequency count.
        freq.clear()
        for clue in clues:
            digit = clue[0]
            freq.setdefault(digit, 0)
            freq[digit] += 1
        # Pick the most frequent leading digit.
        choices = queue.PriorityQueue(len(freq))
        for digit, weight in freq.items():
            choices.put((-weight, digit))
        (w, digit) = choices.get()
        result.append(digit)
        # For each clue whose leading digit matches the selected value, remove
        # the first digit.
        tmp = []
        for clue in clues:
            if len(clue) > 1 and digit == clue[0]:
                tmp.append(clue[1:])
            elif digit != clue[0]:
                tmp.append(clue)
        clues = tmp
    
    print(''.join(result))
