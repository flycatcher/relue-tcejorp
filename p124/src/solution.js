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
var ans = (function(n, i) {
    /**
     * Constructs a new instance of the Radical class
     * 
     * @constructor
     * @this {Radical}
     * @param {number} ub The upperbound (inclusive)
     */
    function Radical(ub) {
        this.radicals_ = new Array(ub + 1);
        this.init_();
    }

    Radical.prototype.init_ = function() {
        var sieve = new Array(this.radicals_.length);
        for (var k = 4; k < sieve.length; k += 2) {
            sieve[k] = 2;
        }
        for (var k = 3, k_max = (sieve.length >> 1); k <= k_max; k += 2) {
            if (sieve[k] !== undefined) {
                continue;
            }
            for (var m = (k << 1); m < sieve.length; m += k) {
                sieve[m] = (sieve[m] === undefined) ? k : sieve[m] * k;
            }
        }
        for (var k = 0; k < sieve.length; k++) {
            if (sieve[k] === undefined) {
                sieve[k] = k;
            }
            this.radicals_[k] = k;
        }
        this.radicals_.sort(function(x, y) {
            var diff = sieve[x] - sieve[y];
            if (diff !== 0) {
                return diff;
            }
            return x - y;
        });
    }

    Radical.prototype.get = function(j) {
        return (j in this.radicals_) ? this.radicals_[j] : 0;
    }

    var radical = new Radical(n);
    return radical.get(i);

})(100000, 10000);

console.log(ans);