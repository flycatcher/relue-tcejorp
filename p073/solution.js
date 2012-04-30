/**
 * Copyright (c) 2012 Jun Mei
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

var ans = (function(n) {
    var a = 0, b = 1, c = 1, d = n;
    var k1 = 0, k2 = 0;
    var term = 1;
    while (c <= n) {
        var k = Math.floor((n + b) / d);
        var p = k * c - a;
        var q = k * d - b;
        a = c, b = d;
        c = p, d = q;
        term += 1;
        // We want to count the number of terms between 1/3 and 1/2.
        if (p == 1 && q == 3) {
            k1 = term;
        } else if (p == 1 && q == 2) {
            k2 = term;
            break;
        }
    }
    return (k2 - k1 - 1);
})(12000);

console.log(ans);