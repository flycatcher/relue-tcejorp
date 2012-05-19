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
     * @constructor
     * @this {Heronian}
     */
    function Heronian() {}

    /**
     * Returns Heronian triplet [a, b, c] such that for a given m
     * 
     * a = m^2 + n^2
     * b = m^2 + n^2
     * c = 4*m*n
     * 
     * If no such n that satisfies these conditions, returns an empty array.
     *
     * @this {Heronian}
     * @private
     * @param {number} x The discriminant for computing n
     * @returns {Array.<number>}
     */
    Heronian.prototype.sides_4mn_ = function(x) {
        var x_sqrt = Math.floor(Math.sqrt(x));
        if (x_sqrt * x_sqrt !== x) {
            return [];
        }
        var n = 2 * m - x_sqrt;
        var a = m * m + n * n,
            c = 4 * m * n;
        return [a, a, c];
    }

    /**
     * Returns Heronian triplet [a, b, c] such that for a given m
     * 
     * a = m^2 + n^2
     * b = m^2 + n^2
     * c = 4*m*n
     * 
     * where a = c + 1. If there is no such n that satisfies these conditions,
     * returns an empty array.
     *
     * @this {Heronian}
     * @private
     * @param {number} m
     * @returns {Array.<number>}
     */
    Heronian.prototype.form1_ = function(m) {
        return this.sides_4mn_(3 * m * m - 1);
    };

    /**
     * Returns Heronian triplet [a, b, c] such that for a given m
     * 
     * a = m^2 + n^2
     * b = m^2 + n^2
     * c = 4*m*n
     * 
     * where a = c - 1. If there is no such n that satisfies these conditions,
     * returns an empty array.
     *
     * @this {Heronian}
     * @private
     * @param {number} m
     * @returns {Array.<number>}
     */
    Heronian.prototype.form2_ = function(m) {
        return this.sides_4mn_(3 * m * m + 1);
    };

    /**
     * Returns Heronian triplet [a, b, c] such that for a given m
     *
     * a = m^2 + n^2
     * b = m^2 + n^2
     * c = 2*(m^2 - n^2)
     *
     * If no such n that satisfies these conditions, returns an empty array.
     *
     * @this {Heronian}
     * @private
     * @param {number} x discriminant for calculating n
     * @returns {Array.<number>}
     */
    Heronian.prototype.sides_2m2n2_ = function(x) {
        if (x < 3 || x % 3 !== 0) {
            return [];
        }
        x = Math.floor(x / 3);
        var x_sqrt = Math.floor(Math.sqrt(x));
        if (x_sqrt * x_sqrt !== x) {
            return [];
        }
        var a = m * m + x,
            c = 2 * (m * m - x);
        return [a, a, c];
    };

    /**
     * Returns Heronian triplet [a, b, c] such that for a given m
     *
     * a = m^2 + n^2
     * b = m^2 + n^2
     * c = 2*(m^2 - n^2)
     *
     * where a = c + 1. If there is no such n that satisfies these conditions,
     * returns an empty array.
     *
     * @this {Heronian}
     * @private
     * @param {number} m
     * @returns {Array.<number>}
     */
    Heronian.prototype.form3_ = function(m) {
        return this.sides_2m2n2_(m * m + 1);
    };

    /**
     * Returns Heronian triplet [a, b, c] such that for a given m
     *
     * a = m^2 + n^2
     * b = m^2 + n^2
     * c = 2*(m^2 - n^2)
     *
     * where a = c - 1. If there is no such n that satisfies these conditions,
     * returns an empty array.
     *
     * @this {Heronian}
     * @private
     * @param {number} m
     * @returns {Array.<number>}
     */
    Heronian.prototype.form4_ = function(m) {
        return this.sides_2m2n2_(m * m - 1);
    };

    Heronian.prototype.sides = function(m) {
        var result = [];
        result.push(this.form1_(m));
        result.push(this.form2_(m));
        result.push(this.form3_(m));
        result.push(this.form4_(m));
        return result;
    };

    var heron = new Heronian();
    var result = 0;

    for (var m = 2, max = Math.sqrt(n / 3); m < max; m++) {
        var sides = heron.sides(m);
        sides.forEach(function(triplets) {
            result += triplets.reduce(function(sum, val) {
                return sum + val;
            }, 0);
        });
    }

    return result;
})(1000000000);

console.log(ans);