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
package org.nevralia;

import java.math.BigInteger;

public class Solution {

    public static void main(String[] args) {
        int result = 0;

        for (int a = 2; a < 100; a++) {
            for (int b = 1; b < 100; b++) {
                BigInteger x = BigInteger.valueOf(a).pow(b);
                int sum = getDigitalSum(x);

                if (sum > result) {
                    result = sum;
                }
            }
        }

        System.out.println(result);
    }

    private static int getDigitalSum(BigInteger x) {
        final BigInteger zero = BigInteger.ZERO;
        final BigInteger ten = BigInteger.TEN;
        int result = 0;

        while (x.compareTo(zero) > 0) {
            BigInteger[] r = x.divideAndRemainder(ten);
            result += r[1].intValue();
            x = r[0];
        }

        return result;
    }
}
