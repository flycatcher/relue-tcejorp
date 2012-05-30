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

using namespace std;

/**
 * Returns a value to indicate whether or not fraction n/m has a terminating
 * decimal form
 */
bool is_terminating(const int& n, int m) {
    if (m <= 0)
        return false;
    if (n % m == 0)
        return true;
    while (m % 2 == 0)
        m /= 2;
    while (m % 5 == 0)
        m /= 5;
    return (m == 1) || (n % m == 0);
}

int main() {
    long ans = 0, n;
    double e = exp(1.0);

#pragma omp parallel for reduction(+:ans)
    for (n = 5; n <= 10000; n++) {
        double x = n / e, x1 = floor(x), x2 = ceil(x);
        int m = (x1 * log(n / x1) > x2 * log(n / x2)) ? (int) x1 : (int) x2;
        ans = ans + (is_terminating(n, m) ? -n : n);
    }

    cout << ans << endl;
    return 0;
}
