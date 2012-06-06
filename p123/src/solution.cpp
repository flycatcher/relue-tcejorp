/*
 * Copyright (c) 2012, Jun Mei
 *
 * Permission is hereby granted, free of charge, to any person obtaining a copy
 * of this software and associated documentation files (the "Software"), to deal
 * in the Software without restriction, including without limitation the rights
 * to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
 * copies of the Software, and to permit persons to whom the Software is
 * furnished to do so, subject to the following conditions:
 *
 * The above copyright notice and this permission notice shall be included in
 * all copies or substantial portions of the Software.
 *
 * THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
 * IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
 * FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
 * AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
 * LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
 * OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
 * SOFTWARE.
 *
 * References:
 *
 * 1. http://en.wikipedia.org/wiki/Sieve_of_Atkin
 */

#include <iostream>
#include <math.h>
#include <vector>

using namespace std;

vector<int> sieve_primes(const int& limit) {
    vector<int> result;
    result.push_back(1); // Place holder for the 0th prime
    if (limit < 2) {
        return result;
    }

    int lng = (limit / 2) - 1 + (limit % 2);
    vector<bool> sieve(lng, true);

    for (int i = 0, sqrt_limit = sqrt(limit) / 2; i < sqrt_limit; i++) {
        if (sieve[i]) {
            int j, inc = 2 * i + 3;
#pragma omp parallel for
            for (j = 2 * i * (i + 3) + 3; j < lng; j += inc) {
                sieve[j] = false;
            }
        }
    }

    result.push_back(2);
    for (int i = 0; i < lng; i++) {
        if (sieve[i]) {
            result.push_back(2 * i + 3);
        }
    }
    return result;
}

int main() {
    const int limit = 10000000;
    vector<int> primes = sieve_primes(limit);
    double log2 = log10(2);
    int ans, size = primes.size();
    for (ans = 1; ans < size; ans += 2) {
        if (log2 + log10(ans) + log10(primes[ans]) > 10) {
            break;
        }
    }
    cout << ans << endl;
    return 0;
}
