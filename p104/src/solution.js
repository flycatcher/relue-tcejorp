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
var ans = (function() {
    /**
     * Constructs a new instance of the NumTools class
     */
    function NumTools() {}

    /**
     * Determines if the given number is 1-9 pandigital
     *
     * @this {NumTools}
     * @constructor
     * @param {number} x The integer to be checked
     * @returns {boolean}
     */
    NumTools.prototype.pandigital = function(x) {
        var digits = [];
        while (x > 0) {
            digits.push(x % 10);
            x = Math.floor(x / 10);
        }
        if (digits.length != 9) {
            return false;
        }
        digits.sort();
        return digits.every(function(val, idx) {
            return (val === idx + 1);
        });
    };

    /**
     * Constructs a new instance of the Fibonacci class
     *
     * @this {Fibonacci}
     * @constructor
     * @param {number} f0
     * @param {number} f1
     * @param {number} mod
     */
    function Fibonacci(f0, f1, mod) {
        this.na_ = f0;
        this.nb_ = f1;
        this.mod_ = mod;
        this.ln_phi_ = Math.log(1 + Math.sqrt(5)) - Math.LN2;
        this.ln_sqrt_5_ = Math.log(5) / 2;
    }

    /**
     * Returns the next Fibonacci number in mod N
     *
     * @this {Fibonacci}
     * @returns {number}
     */
    Fibonacci.prototype.next = function() {
        var n = (this.na_ + this.nb_) % this.mod_;
        this.na_ = this.nb_;
        this.nb_ = n;
        return n;
    };

    Fibonacci.prototype.first = function(n) {
        var a = (n * this.ln_phi_ - this.ln_sqrt_5_) / Math.LN10;
        var b = a - Math.floor(a);
        var c = Math.pow(10, b);
        return Math.floor(c * this.mod_ / 10);
    };

    var fib = new Fibonacci(1, 1, 1000000000);
    var numtools = new NumTools();
    var result = 0;
    var n = 3;

    while (result === 0) {
        var last = fib.next(),
            first = fib.first(n);
        if (numtools.pandigital(last) && numtools.pandigital(first)) {
            result = n;
        }
        n += 1;
    }

    return result;
})();

console.log(ans);