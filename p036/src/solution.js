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
    var isPalindrome = function(x) {
        var size = x.length, mid = size >> 1;
        for (var i = 0; i < mid; i++) {
            if (x[i] !== x[size - i - 1]) {
                return false;
            }
        }
        return true;
    };

    var result = 0;

    for (var num = 1; num < 1000; num++) {
        var head = num.toString(10);
        var tail = (head.length > 1) ? head.slice(0, -1).split("").reverse().join("") : "";
        var x = parseInt(head + tail);

        if (x % 2 === 1 && isPalindrome(x.toString(2))) {
            result += x;
        }

        tail = head.split("").reverse().join("");
        x = parseInt(head + tail);

        if (x % 2 === 1 && isPalindrome(x.toString(2))) {
            result += x;
        }
    }

    return result;
})();

print(ans);
