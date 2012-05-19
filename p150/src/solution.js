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
    function Trigon() {}

    Trigon.prototype.create = function(n) {
        var result = [];
        var t = 0;
        var offset = 1 << 19,
            mod = 1 << 20;
        for (var r = 1; r <= n; r++) {
            var row = [];
            for (var c = 1; c <= r; c++) {
                t = (615949 * t + 797807) % mod;
                row.push(t - offset);
            }
            result.push(row);
        }
        return result;
    };

    Trigon.prototype.min = function(graph, row, col) {
        if (row < col || row >= graph.length) {
            return Number.POSITIVE_INFINITY;
        }
        var result = Number.POSITIVE_INFINITY,
            running_total = 0;
        for (var r = row, r_stop = graph.length; r < r_stop; r++) {
            var list = graph[r];
            for (var c = col, c_stop = col + r - row; c <= c_stop; c++) {
                running_total += list[c];
            }
            if (running_total < result) {
                result = running_total;
            }
        }
        return result;
    };

    Trigon.prototype.key = function(x, y) {
        return x + ":" + y;
    }

    var trigon = new Trigon();
    var graph = trigon.create(n);
    var min_sum = {};
    var r = n - 1;

    graph[r].forEach(function(val, idx) {
        min_sum[trigon.key(r, idx)] = val;
    });

    for (r = n - 2; r >= 0; r--) {
        for (var c = 0; c <= r; c++) {
            var self = trigon.min(graph, r, c);
            var lt = min_sum[trigon.key(r + 1, c)];
            var rt = min_sum[trigon.key(r + 1, c + 1)];
            min_sum[trigon.key(r, c)] = Math.min(self, lt, rt);
        }
    }

    return min_sum[trigon.key(0, 0)];
})(1000);

console.log(ans);