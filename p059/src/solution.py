'''
Created on Apr 24, 2012

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
import itertools

def decode(encoded_text):
    list_and = [ord(x) for x in 'and']
    len_list_and = len(list_and)
    list_the = [ord(x) for x in 'the']
    len_list_the = len(list_the)
    list_an = [ord(x) for x in ' an']
    len_list_an = len(list_an)
    list_it = [ord(x) for x in ' it']
    len_list_it = len(list_it)
    
    codes = [x for x in range(ord('a'), ord('z') + 1)]
    decoder = []
    text_length = len(encoded_text)
    
    for (x1, x2, x3) in itertools.product(codes, repeat=3):
        text = [0] * text_length
        for index in range(0, text_length - 3, 3):
            text[index] = encoded_text[index] ^ x1
            text[index + 1] = encoded_text[index + 1] ^ x2
            text[index + 2] = encoded_text[index + 2] ^ x3
        print(''.join(chr(x) for x in text[:48]))
        if not any((list_and == text[i : i + len_list_and]) for i in range(text_length - len_list_and)):
            continue
        elif not any((list_the == text[i : i + len_list_the]) for i in range(text_length - len_list_the)):
            continue
        elif not any((list_an == text[i : i + len_list_an]) for i in range(text_length - len_list_an)):
            continue
        elif not any((list_it == text[i : i + len_list_it]) for i in range(text_length - len_list_it)):
            continue
        decoder = [x1, x2, x3]
        break
    return decoder

if __name__ == '__main__':
    encoded_text = []
    for line in open(sys.argv[1]):
        s = line.strip()
        if len(s) > 0:
            for token in s.split(','):
                encoded_text.append(int(token))
    decoder = decode(encoded_text)
    text_length = len(encoded_text)
    result = 0
    for index in range(0, text_length):
        result += encoded_text[index] ^ decoder[index % 3]
    print(result)
