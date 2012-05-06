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

import java.util.Arrays;

public class Solution {

    public static void main(String[] args) {
        final int max_width = (1 << 14) + (1 << 13) + (1 << 12);
        final int max_number = max_width * max_width;
        boolean[] sieve = new boolean[max_number];
        Arrays.fill(sieve, true);

        for (int i = 2; i < sieve.length; i++) {
            if (sieve[i]) {
                for (int j = i << 1; j < sieve.length; j += i) {
                    sieve[j] = false;
                }
            }
        }

        int numTotal = 1;
        int numPrimes = 0;

        for (int n = 3; n < max_width; n += 2) {
            numTotal += 4;
            int nSquare = n * n;
            int offset = n - 1;
            for (int j = 1; j <= 3; j++) {
                if (sieve[nSquare - j * offset]) {
                    numPrimes += 1;
                }
            }

            if (numPrimes * 10 < numTotal) {
                System.out.println(n);
                System.exit(0);
            }

            System.out.printf("%d : %d | %d = %f\n", n, numPrimes, numTotal, numPrimes
                    / (1f * numTotal));
        }

        System.out.println("Enlarge width");
    }
}
