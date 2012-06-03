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
#include <math.h>
#include <vector>

using namespace std;

/**
 * Calculates the sum of the square of divisors for each integer less than the
 * given upper bound
 */
vector<long long int> sigma2(const int& limit) {
    vector<long long int> result(limit, 1LL);
    for (long long int i = 2LL; i < limit; i++) {
        long long int n = i * i, j;
#pragma omp parallel for shared(n)
        for (j = i; j < limit; j += i) {
            result[j] += n;
        }
    }
    return result;
}

bool psq(const long long& n) {
    long long sqrt_n = (long long) sqrt(n);
    return (n == sqrt_n * sqrt_n);
}

int main() {
    const int limit = 64000000;
    vector<long long int> sigmas = sigma2(limit);
    long ans = 0L;
    int i;
#pragma omp parallel for reduction(+:ans)
    for (i = 1; i < limit; i++) {
        if (psq(sigmas[i])) {
            ans = ans + i;
        }
    }
    cout << ans << endl;
    return 0;
}
