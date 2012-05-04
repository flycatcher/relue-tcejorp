/**
 * Copyright (c) 2012, Jun Mei
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
 * Source(s):
 * 1. http://mathworld.wolfram.com/PeriodicContinuedFraction.html
 * 2. http://en.wikipedia.org/wiki/Methods_of_computing_square_roots#Continued_fraction_expansion
 */
var ans = (function(n) {
    var expandFractions = function(x) {
        var a0 = Math.floor(Math.sqrt(x));
        var result = [ a0 ];
        if (a0 * a0 === x) {
            return result;
        }
        var m = 0, d = 1, a = a0, a_fin = (a0 << 1);
        while (a !== a_fin) {
            m = d * a - m;
            d = Math.floor((x - m * m) / d);
            a = Math.floor((a0 + m) / d);
            result.push(a);
        }
        return result;
    };

    var result = 0, i;
    for (i = 1; i <= n; i++) {
        var length = expandFractions(i).length;
        if (length > 1 && length % 2 === 0) {
            result += 1;
        }
    }
    return result;
})(10000);

console.log(ans);