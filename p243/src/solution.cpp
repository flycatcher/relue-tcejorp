/** 
 * Copyright (c) 2012, Jun Mei
 *
 * Permission is hereby granted, free of charge, to any person obtaining a copy
 * of this software and associated documentation files (the "Software"), to
 * deal in the Software without restriction, including without limitation the
 * rights to use, copy, modify, merge, publish, distribute, sublicense, and/or
 * sell copies of the Software, and to permit persons to whom the Software is
 * furnished to do so, subject to the following conditions:
 *
 * The above copyright notice and this permission notice shall be included in
 * all copies or substantial portions of the Software.
 *
 * THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
 * IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
 * FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
 * AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
 * LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
 * FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS
 * IN THE SOFTWARE.
 *
 * References:
 *
 * 1. http://en.wikipedia.org/wiki/Euler%27s_totient_function
 * 2. http://en.wikipedia.org/wiki/Sieve_of_Atkin
 */

#include <iostream>
#include <math.h>
#include <vector>

using namespace std;

vector<int> sieve_primes(const int& limit) {
    vector<int> result;

    if (limit < 2) {
        return result;
    }

    int m = (limit / 2) - 1 + (limit % 2);
    vector<bool> sieve(m, true);

    for (int i = 0, sqrt_limit = sqrt(limit) / 2; i < sqrt_limit; i++) {
        if (sieve[i]) {
            int j, inc = 2 * i + 3;
            for (j = 2 * i * (i + 3) + 3; j < m; j += inc) {
                sieve[j] = false;
            }
        }
    }

    result.push_back(2);
    for (int i = 0; i < m; i++) {
        if (sieve[i]) {
            result.push_back(2 * i + 3);
        }
    }
    return result;
}

int main() {
    const int limit = 50;
    vector<int> primes = sieve_primes(limit);
    long totient = 1L, ans = 1L, lt = 1L;

    for (vector<int>::iterator it = primes.begin(); it != primes.end(); it++) {
        int p = *it;
        lt = totient * (p - 1) * 94744L;
        if (lt < (ans * p - 1) * 15499L) {
            break;
        }
        totient *= (p - 1), ans *= p;
    }

    lt = totient * 94744L;
    while (lt >= (ans - 1) * 15499L) {
        lt *= 2L, ans *= 2L;
    }

    cout << ans << endl;
    return 0;
}
