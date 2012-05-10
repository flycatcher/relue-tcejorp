/**
 * @license Copyright (c) 2012, Jun Mei
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
 * OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
 * THE SOFTWARE.
 */
var ans = (function(n) {
    /**
     * Initializes a new instance of the Primes class
     *
     * @this {Primes}
     */
    function Primes() {}

    /**
     * Returns all prime numbers less than a given number
     *
     * @this {Primes}
     * @param {number} m All primes below this number
     * @returns {Array.<number>}
     */
    Primes.prototype.sieve = function(m) {
        var primes = new Array(m);
        for (var x = 4; x < m; x += 2) {
            primes[x] = false;
        }
        var m_max = Math.sqrt(m) | 0;
        for (var x = 3; x <= m_max; x += 2) {
            if (primes[x] === undefined) {
                for (var y = (x << 1); y < m; y += x) {
                    primes[y] = false;
                }
            }
        }
        var result = [];
        for (var x = 2; x < m; x++) {
            if (primes[x] === undefined) {
                result.push(x);
            }
        }
        return result;
    };

    var primes = (new Primes()).sieve(n);
    var result = 0;

    if (n > 16) {
        result += 2;
    } else if (n > 4) {
        result += 1;
    }

    var max_16 = (n / 16) | 0,
        max_4 = (n / 4) | 0;

    // Remove 2 because we are interested in odd primes only
    primes.shift();

    primes.forEach(function(prime) {
        if (prime % 4 === 3) result += 1;
        if (prime <= max_16) result += 2;
        else if (prime <= max_4) result += 1;
    });

    return result;
})(50000000);

console.log(ans);