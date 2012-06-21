/**
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
 * 1. http://thales.math.uqam.ca/~rowland/papers/The_number_of_nonzero_binomial_
 * coefficients_modulo_p%5Ealpha.pdf
 * 2. Nathan Fine, Binomial coefficients modulo a prime, The American
 * Mathematical Monthly 54 (1947) 589–592.
 */

#include <iostream>

using namespace std;

/**
 * Returns the number of non-zero terms in the first n rows of the Pascal's
 * triangle modulo a particular prime; this method uses Fine's theorem
 */
unsigned long fine(unsigned int n, const unsigned int& prime) {
    unsigned long result = 0L;
    if (n > 0) {
        unsigned int p = prime * (prime + 1) / 2;
        unsigned long m = 1, r = 1;
        while (m * prime < n) {
            m = m * prime;
            r = r * p;
        }
        unsigned int x = n / m;
        result = r * x * (x + 1) / 2 + (x + 1) * fine(n % m, prime);
    }
    return result;
}

int main() {
    const unsigned int n = 1000000000, p = 7;
    unsigned long ans = fine(n, p);
    cout << ans << endl;
    return 0;
}
