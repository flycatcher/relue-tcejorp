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
 */
var ans = (function() {
    var digitize = function(x) {
        var digits = [];
        while (x > 0) {
            digits.push(x % 10);
            x = Math.floor(x / 10);
        }
        if (digits.length > 1) {
            digits.reverse();
        }
        return digits;
    };

    var next = function(position, number) {
        var numDigits = digitize(number).length;
        var nextNumber = Math.floor(Math.pow(10, numDigits));
        var numericDistance = nextNumber - number;
        var nextPosition = position + numericDistance * numDigits;
        var positionStep = digitize(position).length;
        var nextPositionCheckpoint = Math.floor(Math.pow(10, positionStep));

        if (nextPosition > nextPositionCheckpoint) {
            var positionDistance = nextPositionCheckpoint - position;
            nextNumber = number + Math.floor(positionDistance / numDigits);
            nextPosition = position + numDigits * Math.floor(positionDistance / numDigits);
        }

        return [ nextPosition, nextNumber ];
    };

    var result = 1;
    var number = 1;
    var position = 1;
    var checkpoints = [ 1, 10, 100, 1000, 10000, 100000, 1000000 ];
    var max = checkpoints.reduce(function(max, value) {
        return (value > max) ? value : max;
    }, 0);

    while (position <= max) {
        var digits = digitize(number);
        var isChecked = false;

        for ( var index = 0; index < digits.length; index++) {
            if (checkpoints.indexOf(position + index) >= 0) {
                result *= digits[index];
                isChecked = true;
                break;
            }
        }

        if (isChecked) {
            position += digits.length;
            number += 1;
        } else {
            var nextPositionNumber = next(position, number);
            position = nextPositionNumber[0];
            number = nextPositionNumber[1];
        }
    }

    return result;
})();

print(ans);