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
 * OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
 * SOFTWARE.
 * 
 * Reference:
 * 
 * 1. http://mathworld.wolfram.com/PellEquation.html
 */
var ans = (function(n) {
    /**
     * Pell Equation of the form x^2 - D*y^2 = 1
     * 
     * @constructor
     * @this {Pell}
     * @param {number}
     *            d Coefficient D of the Pell Equation; expected to be a
     *            natural, square-free number
     */
    function Pell(d) {
        this.d_ = d;
    }

    /**
     * Returns the fundamental solution [x, y] where x is minimized
     * 
     * @this {Pell}
     * @returns {Array.<number>}
     */
    Pell.prototype.solve = function() {
        var a0 = Math.floor(Math.sqrt(this.d_));
        if (a0 * a0 === this.d_) {
            // No fundamental solution when D is a perfect square
            return [ 1, 0 ];
        }
        var m = 0, d = 1, a = a0;
        var x = a0, y = 1, x_last = 1, y_last = 0, x_next, y_next;
        var term = 1;
        // The fundamental solution has to be an odd term in the continued
        // fraction expansion where the next term indicates the start of a new
        // periodic cycle (i.e. a == 2 * a0).
        while (a !== (a0 << 1) || term % 2 === 0) {
            m = a * d - m;
            d = Math.floor((this.d_ - m * m) / d);
            a = Math.floor((a0 + m) / d);
            x_next = a * x + x_last;
            y_next = a * y + y_last;
            x_last = x, y_last = y;
            x = x_next, y = y_next;
            term += 1;
        }
        return [ x_last, y_last ];
    };

    var max = 0, d, result;
    for (d = 1; d <= n; d++) {
        var x = (new Pell(d)).solve()[0];
        if (x > max) {
            max = x;
            result = d;
        }
    }

    return result;
})(1000);

console.log(ans);
