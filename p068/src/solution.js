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
     * Constructs an instance of the Itertools class
     *
     * @this {Itertools}
     */
    function Itertools() {}

    /**
     * Computes the next permutation in lexicographic order
     *
     * @this {Itertools}
     * @param {Array.<number>} lst The list of numbers that will be updated to
     * the next lexicographic order
     * @returns {boolean} true if the next permutation is obtained; otherwise,
     * false
     */
    Itertools.prototype.permute = function(lst) {
        var k = lst.reduceRight(function(prev, value, idx, self) {
            return (prev < 0 && idx > 0 && self[idx - 1] < value) ? idx - 1 : prev;
        }, -1);
        if (k === -1) {
            return false;
        }
        var lst_k = lst[k];
        var l = lst.reduce(function(prev, value, idx) {
            return (value > lst_k) ? idx : prev;
        }, k + 1);
        lst[k] = lst[l], lst[l] = lst_k;
        lst.splice(k + 1).reverse().forEach(function(value) {
            lst.push(value);
        });
        return true;
    };

    function MagicRing(n) {
        /**
         * @private {number}
         */
        this.fixed_ = n;
    }

    /**
     * Tests if the given list of numbers solves the 5-gon ring
     *
     * @this {MagicRing}
     * @param {Array.<number>} lst
     * @returns {boolean}
     */
    MagicRing.prototype.test = function(lst) {
        var ref = this.fixed_ + lst[0] + lst[1];
        var line = lst[5] + lst[1] + lst[2];
        if (ref !== line) return false;
        line = lst[6] + lst[2] + lst[3];
        if (ref !== line) return false;
        line = lst[7] + lst[3] + lst[4];
        if (ref !== line) return false;
        line = lst[8] + lst[4] + lst[0];
        if (ref !== line) return false;
        return true;
    }

    /**
     * Formats the given list of numbers in accordance with the requirements of
     * a valid solution set (leading number must be minimal); it is assumed that
     * the fixed number is on the outer edge
     *
     * @this {MagicRing}
     * @param {Array.<number>} lst
     * @returns {string}
     */
    MagicRing.prototype.format = function(lst) {
        var set = [];
        set.push([lst[5], lst[1], lst[2]].join(""));
        set.push([lst[6], lst[2], lst[3]].join(""));
        set.push([lst[7], lst[3], lst[4]].join(""));
        set.push([lst[8], lst[4], lst[0]].join(""));
        set.push([this.fixed_, lst[0], lst[1]].join(""));
        var shifts = lst.slice(5).reduce(function(prev, value, idx, self) {
            return (value < self[prev]) ? idx : prev;
        }, 0);
        while (shifts > 0) {
            var line = set.shift();
            set.push(line);
            shifts -= 1;
        }
        return set.join("");
    }

    var numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9];
    var itertools = new Itertools();
    var ring = new MagicRing(10);
    var solutions = [];

    while (itertools.permute(numbers)) {
        if (ring.test(numbers)) {
            solutions.push(ring.format(numbers));
        }
    }

    return solutions.reduce(function(prev, value) {
        return (value > prev) ? value : prev;
    }, "");
})();

console.log(ans);