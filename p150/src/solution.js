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
     * Constructs a new instance of the Trigon class
     *
     * @constructor
     * @this {Trigon}
     * @param {number} n Number of rows
     */
    function Trigon(n) {
        /**
         * A jagged array that represents the whole triangle
         * @private
         * @type {Array.<Array.<number>>}
         */
        this.graph_ = new Array(n);
        /**
         * A jagged array that represents the culmulative sum of all numbers in
         * a row up till (and including) that particular column
         * @private
         * @type {Array.<Array.<number>>}
         */
        this.row_sum_ = new Array(n);
        this.init_(n);
    }

    /**
     * Initializes numeric representations and row sums
     * 
     * @private
     * @this {Trigon}
     * @param {number} n Number of rows
     */
    Trigon.prototype.init_ = function(n) {
        var t = 0;
        var offset = 1 << 19,
            mod = 1 << 20;
        for (var r_idx = 0; r_idx < n; r_idx++) {
            var row = new Array(r_idx + 1),
                sum = new Array(r_idx + 1);
            for (var c_idx = 0; c_idx <= r_idx; c_idx++) {
                t = (615949 * t + 797807) % mod;
                row[c_idx] = (t - offset);
                sum[c_idx] = row[c_idx];
                if (c_idx > 0) {
                    sum[c_idx] += sum[c_idx - 1];
                }
            }
            this.graph_[r_idx] = row;
            this.row_sum_[r_idx] = sum;
        }
    };

    /**
     * Returns the minimum sum among all sub-triangles that contain the given
     * row and column indices as the starting point
     *
     * @this {Trigon}
     * @param {number} row The starting row index
     * @param {number} col The starting column index
     * @returns {number}
     */
    Trigon.prototype.min = function(row, col) {
        var result = Number.POSITIVE_INFINITY;
        if (row < col || row >= this.graph_.length) {
            return result;
        }
        var total = 0;
        for (var r = row, r_stop = this.row_sum_.length; r < r_stop; r++) {
            var sum = this.row_sum_[r];
            total += sum[col + r - row] - sum[col];
            if (total < result) {
                result = total;
            }
        }
        return result;
    };

    Trigon.prototype.key = function(x, y) {
        return x + ":" + y;
    };

    var trigon = new Trigon(n);
    var min_sum = {};
    var r = n - 1, c;

    for (c = 0; c <= r; c++) {
        min_sum[trigon.key(r, c)] = trigon.min(r, c);
    }

    for (r = n - 2; r >= 0; r--) {
        for (c = 0; c <= r; c++) {
            var sf = trigon.min(r, c),
                lt = min_sum[trigon.key(r + 1, c)],
                rt = min_sum[trigon.key(r + 1, c + 1)];
            min_sum[trigon.key(r, c)] = Math.min(sf, lt, rt);
        }
    }

    return min_sum[trigon.key(0, 0)];
})(1000);

console.log(ans);