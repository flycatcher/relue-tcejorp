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
    var max = Math.pow(2, 15) - 1;
    var sieve = new Array(max);

    for ( var i = 0; i < max; i++) {
        sieve[i] = 0;
    }

    sieve.forEach(function(element, index, array) {
        if (index > 0) {
            for ( var i = index << 1; i < array.length; i += index) {
                array[i] += index;
            }
        }
    });

    var naturals = new Array(max);

    for ( var i = 0; i < max; i++) {
        naturals[i] = false;
    }

    sieve.map(function(divisors, num) {
        return (divisors > num) ? num : 0;
    }).filter(function(num) {
        return (num > 0);
    }).forEach(function(num, index, array) {
        for ( var i = index; i < array.length; i++) {
            var x = num + array[i];
            if (x < naturals.length) {
                naturals[x] = true;
            }
        }
    });

    var result = naturals.reduce(function(sum, value, index) {
        return (value) ? sum : sum + index;
    }, 0);

    return result;
})();

print(ans);