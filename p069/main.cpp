// Copyright (c) 2012, Jun Mei
// 
// Permission is hereby granted, free of charge, to any person obtaining a copy of
// this software and associated documentation files (the "Software"), to deal in
// the Software without restriction, including without limitation the rights to
// use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of
// the Software, and to permit persons to whom the Software is furnished to do so,
// subject to the following conditions:
// 
// The above copyright notice and this permission notice shall be included in all
// copies or substantial portions of the Software.
// 
// THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
// IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS
// FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR
// COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER
// IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN
// CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

#include <iostream>

int main (int argc, char * const argv[]) {
    const int upperbound = 100;
    bool sieve[upperbound] = { false };
    
    for (int i = 2; i < upperbound; i++) {
        if (sieve[i] == false) {
            for (int j = (i << 1); j < upperbound; j += i) {
                sieve[j] = true;
            }
        }
    }
    
    int result = 2;
    
    for (int i = 3; i < upperbound; i += 2) {
        if (result * i >= 1000000) {
            break;
        } else if (sieve[i] == false) {
            result *= i;
        }
    }
    
    std::cout << result << "\n";
    return 0;
}
