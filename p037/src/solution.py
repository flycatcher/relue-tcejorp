'''
Created on Apr 22, 2012

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

def is_prime(number, primes):
    upper_bound = math.sqrt(number)
    for prime in primes:
        if prime > upper_bound:
            break
        elif number % prime == 0:
            return False
    return True

def main(max_primes):
    primes = [2, 3, 5, 7]
    prime_set = set(primes)
    number = max(primes)
    count = 0
    result = 0
    
    while count < max_primes:
        number += 2
        if is_prime(number, primes) == False:
            continue
        primes.append(number)
        prime_set.add(number)
        s = str(number)
        is_ok = True
        for end in range(1, len(s)):
            if int(s[:end]) not in prime_set:
                is_ok = False
                break
        if is_ok:
            for start in range(1, len(s)):
                if int(s[start:]) not in prime_set:
                    is_ok = False
                    break
        if is_ok:
            count += 1
            result += number
            print(number)
    print(result)

if __name__ == '__main__':
    main(11)
