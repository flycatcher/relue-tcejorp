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
import java.util.Collection;
import java.util.List;

public class Solution {

    public static void main(String[] args) {
        long num = 600851475143L;
        double sqrt = Math.sqrt(num);
        List<Long> primes = getPrimesLessThan(Math.round(sqrt));
        for (int i = primes.size() - 1; i >= 0; --i) {
            if (num % primes.get(i) == 0) {
                System.out.println(primes.get(i));
                System.exit(0);
            }
        }
    }

    /**
     * Returns all prime numbers less than the given number
     * 
     * @param max
     * @return
     */
    private static List<Long> getPrimesLessThan(long max) {
        List<Long> result = new ArrayList<Long>();
        result.add(2L);
        long num = 3;

        while (num < max) {
            if (isPrime(num, result)) {
                result.add(num);
            }

            num += 2;
        }

        return result;
    }

    private static boolean isPrime(long num, Collection<Long> primes) {
        double cutOff = Math.sqrt(num);

        for (long prime : primes) {
            if (prime > cutOff) {
                break;
            } else if (num % prime == 0) {
                return false;
            }
        }

        return true;
    }
}
