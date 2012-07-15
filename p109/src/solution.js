/**
 * @license Copyright (C) 2012, Jun Mei
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
 */
var ans = (function(a, b) {
    function Darts() {}

    Darts.prototype.checkout = function() {
        var i, singles = [], doubles = [], triples = [];
        for (i = 1; i <= 20; i++) {
            singles.push(i);
            doubles.push(2 * i);
            triples.push(3 * i);
        }
        singles.push(25);
        doubles.push(50);

        var result = {};
        var shots = singles.concat(doubles, triples);
        // Checks out with only one dart
        doubles.forEach(function(x) {
            result[x] = 1;
        });
        // Checks out with two darts
        shots.forEach(function(x) {
            doubles.forEach(function(y) {
                var n = x + y;
                if (n in result) {
                    result[n] += 1;
                } else {
                    result[n] = 1;
                }
            });
        });
        // Checks out with three darts
        shots.forEach(function(x, index, self) {
            self.slice(index).forEach(function(y) {
                doubles.forEach(function(z) {
                    var n = x + y + z;
                    if (n in result) {
                        result[n] += 1;
                    } else {
                        result[n] = 1;
                    }
                });
            });
        });

        return result;
    };

    var darts = new Darts();
    var counts = darts.checkout();
    var result = Object.keys(counts).reduce(function(previous, x) {
        var score = parseInt(x);
        return (score > a && score < b) ? previous + counts[x] : previous;
    }, 0);
    return result;
})(1, 100);

console.log(ans);