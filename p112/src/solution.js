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
    function NumTools() {}

    /**
     * Determines if the given number is a "bouncy number"
     *
     * @this {NumTools}
     * @param {number} x The number to be checked
     * @returns {boolean}
     */
    NumTools.prototype.isBouncy = function(x) {
        var digits = [];
        while (x > 0) {
            digits.unshift(x % 10);
            x = (x / 10) | 0;
        }
        var isIncreasing = digits.every(function(value, idx, self) {
            return (idx > 0) ? value >= self[idx - 1] : true;
        });
        var isDecreasing = digits.every(function(value, idx, self) {
            return (idx > 0) ? value <= self[idx - 1] : true;
        });
        return (isIncreasing === false) && (isDecreasing === false);
    };

    var numtools = new NumTools();
    var group = 100,
        result = 100,
        bouncies = 0;

    do {
        for (var x = 1; x <= group; x++) {
            if (numtools.isBouncy(++result)) {
                bouncies += 1;
            }
        }
    } while ((result - bouncies) !== ((result / group) | 0));

    return result;
})();

console.log(ans);