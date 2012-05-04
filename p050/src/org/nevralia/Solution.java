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

import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashSet;
import java.util.List;
import java.util.Set;

public class Solution {

    public static void main(String[] args) {
        final int upperbound = 1000000;

        List<Integer> primeSums = getPrimesLessThan(upperbound);
        Set<Integer> primeSet = new HashSet<Integer>(primeSums);
        int numOfTerms = 0;
        int result = 0;

        for (int i = 1; i < primeSums.size(); i++) {
            int prime = primeSums.get(i);

            for (int j = i - 1; j >= 0; j--) {
                int sum = prime + primeSums.get(j);

                if (sum > upperbound) {
                    break;
                }

                primeSums.set(j, sum);

                if (primeSet.contains(sum) && numOfTerms < i - j + 1) {
                    numOfTerms = i - j + 1;
                    result = sum;
                }
            }
        }

        System.out.printf("%d = sum of %d consecutive primes\n", result, numOfTerms);
    }

    private static List<Integer> getPrimesLessThan(final int number) {
        boolean[] sieve = new boolean[number];
        Arrays.fill(sieve, true);
        ArrayList<Integer> result = new ArrayList<Integer>();
        for (int i = 2; i < sieve.length; i++) {
            if (sieve[i]) {
                result.add(i);
                for (int j = i << 1; j < sieve.length; j += i) {
                    sieve[j] = false;
                }
            }
        }
        return result;
    }
}
