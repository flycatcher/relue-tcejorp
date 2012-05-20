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
 */
var ans = (function() {
    var factorials = [];
    factorials.push(1);
    for (var i = 1; i <= 9; i++) {
        var next = factorials[i - 1] * i;
        factorials.push(next);
    }

    var getDigits = function(x) {
        var digits = [];
        while (x > 0) {
            digits.push(x % 10);
            x = Math.floor(x / 10);
        }
        return digits;
    };

    var result = 0;
    var max = 7 * factorials[9];

    for (var i = 10; i <= max; i++) {
        var total = getDigits(i).reduce(function(sum, value) {
            return sum + factorials[value];
        }, 0);

        if (total === i) {
            result += i;
        }
    }

    return result;
})();

print(ans);
