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
#include <map>
#include <math.h>
#include <numeric>
#include <set>
#include <vector>

using namespace std;

/**
 * Computes all prime number less than a given limit and returns them in order
 */
vector<int> sp(const int& limit) {
    vector<bool> sieve(limit, true);
    double sqrt_limit = sqrt(limit);

    for (int i = 3; i <= sqrt_limit; i += 2) {
        if (sieve[i]) {
            for (int j = i * i; j < limit; j += i) {
                sieve[j] = false;
            }
        }
    }

    vector<int> result;
    if (limit > 2) {
        result.push_back(2);
    }
    for (int i = 3; i < limit; i += 2) {
        if (sieve[i]) {
            result.push_back(i);
        }
    }

    return result;
}

map<int, vector<int> > fp(const int& limit, const vector<int>& primes) {
    map<int, vector<int> > result;
    int p, size = primes.size();
    for (p = 0; p < size; p++) {
        int prime = primes[p];
        vector<int> powers(limit, 0);
        for (int m = prime; m < limit; m *= prime) {
            for (int n = 2; n < limit; n++) {
                powers[n] += (n / m);
            }
        }
        result[prime] = powers;
    }
    return result;
}

/**
 * Computes and returns the binomial coefficient C(n, m)
 */
long binomial(const int& n, const int& m) {
    long result = 1L, diff = n - m;
    if (diff >= n || diff <= 0L) {
        return result;
    }
    for (long i = 1L; i <= m; i++) {
        result *= diff + i;
        result /= i;
    }
    return result;
}

int main() {
    const int limit = 51;
    vector<int> primes = sp(limit);
    map<int, vector<int> > powers = fp(limit, primes);
    set<long> binomials;
    for (int n = 2; n < limit; n++) {
        for (int m = 1; m <= n / 2; m++) {
            bool isSquareFree = true;
            map<int, vector<int> >::iterator it;
            for (it = powers.begin(); it != powers.end(); it++) {
                vector<int> fps = (*it).second;
                int p = fps[n] - fps[n - m] - fps[m];
                if (p > 1) {
                    isSquareFree = false;
                    break;
                }
            }
            if (isSquareFree) {
                binomials.insert(binomial(n, m));
            }
        }
    }
    long ans = accumulate(binomials.begin(), binomials.end(), 1L);
    cout << ans << endl;
    return 0;
}
