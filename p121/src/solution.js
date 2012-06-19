/**
 * @license Copyright (C) 2012, Jun Mei
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
var ans = (function(n) {
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

    function Chance() {}

    Chance.prototype.prob = function(seq) {
        var result = seq.reduce(function(previousValue, currentValue, index) {
            var blue = 1.0 / (index + 2);
            var mul = (currentValue === 1) ? blue : 1 - blue;
            return previousValue * mul;
        }, 1);
        return result;
    }

    var itertools = new Itertools();
    var chance = new Chance();
    var m;
    var result = 0;
    for (m = (n >> 1) + 1; m <= n; m++) {
        var o = []
        var i;
        for (i = 1; i <= m; i++) {
            o.push(1);
        }
        for (i = m; i < n; i++) {
            o.push(0);
        }
        o.reverse();
        do {
            result += chance.prob(o);
        } while (itertools.permute(o));
    }
    return Math.floor(1.0 / result);
})(15);

console.log(ans);