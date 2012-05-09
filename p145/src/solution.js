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
    function Numbers() {}

    Numbers.prototype.reversible = function(x) {
        if (x % 10 === 0) {
            return false;
        }
        var x_copy = x;
        var y = 0;
        while (x_copy > 0) {
            y *= 10;
            y += (x_copy % 10);
            x_copy = Math.floor(x_copy / 10);
        }
        var z = x + y;
        while (z > 0) {
            if (z % 2 === 0) {
                return false;
            }
            z = Math.floor(z / 10);
        }
        return true;
    };

    var result = 0;
    var numbers = new Numbers();

    for (var i = 1; i < n; i++) {
        if (numbers.reversible(i)) {
            result += 1;
        }
    }

    return result;
})(1000000000);

console.log(ans);