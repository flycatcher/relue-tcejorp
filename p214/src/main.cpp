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
 */
#include <iostream>
#include <vector>

using namespace std;

vector<int> sieve_totients(const int& limit) {
    vector<int> result(limit, 0);
    int i;
#pragma omp parallel for
    for (i = 0; i < limit; i++) {
        result[i] = i;
    }
#pragma omp parallel for
    for (i = 2; i < limit; i += 2) {
        result[i] = (result[i] >> 1);
    }
    for (i = 3; i < limit; i += 2) {
        if (result[i] == i) {
            int j;
#pragma omp parallel for shared(i)
            for (j = i; j < limit; j += i) {
                result[j] = result[j] - (result[j] / i);
            }
        }
    }
    return result;
}

/**
 * Calculates and returns the totient chain size for a given integer p
 */
int chain_size(const int& p, const vector<int>& totients) {
    int result = 1, n = p;
    while (n > 1) {
        result += 1;
        n = totients[n];
    }
    return result;
}

int main() {
    const int limit = 40000000, target_size = 25;
    vector<int> phi = sieve_totients(limit);
    int n;
    long ans = 0L;
#pragma omp parallel for shared(phi) reduction(+:ans)
    for (n = 3; n < limit; n += 2) {
        if (phi[n] + 1 == n && chain_size(n, phi) == target_size) {
            ans = ans + n;
        }
    }
    cout << ans << endl;
    return 0;
}
