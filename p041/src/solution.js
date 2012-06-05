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
    var isPrime = function(x, primes) {
        var threshold = Math.sqrt(x);
        var isComposite = primes.some(function(prime) {
            return (prime <= threshold) && (x % prime === 0);
        });
        return (isComposite === false);
    };

    var getPrimes = function(max) {
        var primes = [];
        primes.push(2);
        var num = 3;

        while (num < max) {
            if (isPrime(num, primes)) {
                primes.push(num);
            }
            num += 2;
        }

        return primes;
    };

    var getDigits = function(x) {
        var digits = [];
        while (x > 0) {
            digits.push(x % 10);
            x = Math.floor(x / 10);
        }
        return digits;
    };

    var isPandigital = function(x) {
        var digits = getDigits(x);
        digits.sort();
        return digits.every(function(value, index) {
            return (value === index + 1);
        });
    };

    var primes = getPrimes(987654321);
    var result = 0;

    for ( var i = primes.length - 1; i >= 0; i--) {
        if (isPandigital(primes[i])) {
            result = primes[i];
            break;
        }
    }

    return result;
})();

print(ans);