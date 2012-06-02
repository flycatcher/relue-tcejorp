'''
Created on May 1, 2012

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
import sys

def is_flush(cards):
    suits = set(x[1] for x in cards)
    return len(suits) == 1

def is_royal_flush(cards):
    result = (sorted(x[0] for x in cards) == ['A', 'J', 'K', 'Q', 'T'])
    result = result and is_flush(cards)
    return result

def win_by_royal_flush(first, second):
    f, s = is_royal_flush(first), is_royal_flush(second)
    if f and not s:
        return 1
    elif not f and s:
        return -1
    return 0

def is_straight(cards):
    faces = 'AKQJT98765432A'
    c = set(x[0] for x in cards)
    for idx in range(len(faces) - 5):
        s = set(x for x in faces[idx:idx + 5])
        if s == c:
            return True
    return False

def win_by_straight_flush(first, second):
    f = is_straight(first) and is_flush(first)
    s = is_straight(second) and is_flush(second)
    if f and not s:
        return 1
    elif not f and s:
        return -1
    return 0

def face_pattern(cards):
    f = list(x[0] for x in cards)
    c = set(f)
    return sorted(map(lambda x: f.count(x), c))

def is_four_of_kind(cards):
    return face_pattern(cards) == [1, 4]

def win_by_four_of_kind(first, second):
    f = is_four_of_kind(first)
    s = is_four_of_kind(second)
    if f and not s:
        return 1
    elif not f and s:
        return -1
    elif f and s:
        for c in 'AKQJT98765432':
            if first.count(c) == 4:
                return 1
            elif second.count(c) == 4:
                return -1
    return 0

def is_full_house(cards):
    return face_pattern(cards) == [2, 3]

def win_by_full_house(first, second):
    f = is_full_house(first)
    s = is_full_house(second)
    if f and not s:
        return 1
    elif not f and s:
        return -1
    elif f and s:
        for c in 'AKQJT98765432':
            if first.count(c) == 3:
                return 1
            elif second.count(c) == 3:
                return -1
    return 0

def win_by_flush(first, second):
    f = is_flush(first)
    s = is_flush(second)
    if f and not s:
        return 1
    elif not f and s:
        return -1
    return 0

def win_by_straight(first, second):
    f = is_straight(first)
    s = is_straight(second)
    if f and not s:
        return 1
    elif s and not f:
        return -1
    else:
        faces = 'AKQJT98765432A'
        f = set(x[0] for x in first)
        s = set(x[0] for x in second)
        for idx in range(len(faces) - 5):
            c = set(x for x in faces[idx:idx + 5])
            if c == f and c != s:
                return 1
            elif c != f and c == s:
                return -1
    return 0

def is_three_of_kind(cards):
    return face_pattern(cards) == [1, 1, 3]

def win_by_three_of_kind(first, second):
    f = is_three_of_kind(first)
    s = is_three_of_kind(second)
    if f and not s:
        return 1
    elif not f and s:
        return -1
    elif f and s:
        f = list(x[0] for x in first)
        s = list(x[0] for x in second)
        for c in 'AKQJT98765432':
            if f.count(c) == 3:
                return 1
            elif s.count(c) == 3:
                return -1
    return 0

def is_two_pairs(cards):
    return face_pattern(cards) == [1, 2, 2]

def win_by_two_pairs(first, second):
    f = is_two_pairs(first)
    s = is_two_pairs(second)
    if f and not s:
        return 1
    elif not f and s:
        return -1
    elif f and s:
        f = list(x[0] for x in first)
        s = list(x[0] for x in second)
        for c in 'AKQJT98765432':
            if f.count(c) == 2 and s.count(c) < 2:
                return 1
            elif f.count(c) < 2 and s.count(c) == 2:
                return -1
    return 0

def is_one_pair(cards):
    return face_pattern(cards) == [1, 1, 1, 2]

def win_by_one_pair(first, second):
    f = is_one_pair(first)
    s = is_one_pair(second)
    if f and not s:
        return 1
    elif not f and s:
        return -1
    elif f and s:
        f = list(x[0] for x in first)
        s = list(x[0] for x in second)
        for c in 'AKQJT98765432':
            if f.count(c) == 2 and s.count(c) < 2:
                return 1
            elif f.count(c) < 2 and s.count(c) == 2:
                return -1
    return 0

def win_by_high_card(first, second):
    f = sorted(x[0] for x in first)
    s = sorted(x[0] for x in second)
    for x in 'AKQJT98765432':
        while x in f:
            f.remove(x)
        while x in s:
            s.remove(x)
        if len(f) < len(s):
            return 1
        elif len(f) > len(s):
            return -1
    return 0

def count_winning_hands(rounds):
    result = 0
    for (first, second) in rounds:
        ruling = win_by_royal_flush(first, second)
        if ruling == 0:
            ruling = win_by_straight_flush(first, second)
        if ruling == 0:
            ruling = win_by_four_of_kind(first, second)
        if ruling == 0:
            ruling = win_by_full_house(first, second)
        if ruling == 0:
            ruling = win_by_flush(first, second)
        if ruling == 0:
            ruling = win_by_straight(first, second)
        if ruling == 0:
            ruling = win_by_three_of_kind(first, second)
        if ruling == 0:
            ruling = win_by_two_pairs(first, second)
        if ruling == 0:
            ruling = win_by_one_pair(first, second)
        if ruling == 0:
            ruling = win_by_high_card(first, second)
        if ruling > 0:
            result += 1
    return result

if __name__ == '__main__':
    rounds = []
    for line in open(sys.argv[1]):
        line_clean = line.strip().upper()
        if len(line_clean) == 0:
            continue
        tokens = line_clean.split(' ')
        if len(tokens) == 10:
            rounds.append((tokens[0:5], tokens[5:10]))
    ans = count_winning_hands(rounds)
    print(ans)
