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
import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class Solution {

    public static void main(String[] args) {
        int maxNum = 31;
        Collection<Integer> primes = getPrimesLessThan(maxNum);
        Map<Integer, Integer> factors = new HashMap<Integer, Integer>();

        for (int i = 2; i < maxNum; i++) {
            Map<Integer, Integer> fs = factorize(i, primes);

            for (Map.Entry<Integer, Integer> entry : fs.entrySet()) {
                if (factors.containsKey(entry.getKey())) {
                    int count = Math.max(factors.get(entry.getKey()), entry.getValue());
                    factors.put(entry.getKey(), count);
                } else {
                    factors.put(entry.getKey(), entry.getValue());
                }
            }
        }

        long result = 1L;

        for (Map.Entry<Integer, Integer> entry : factors.entrySet()) {
            result *= Math.pow(entry.getKey(), entry.getValue());
        }

        System.out.println(result);
    }

    private static Map<Integer, Integer> factorize(int x, Collection<Integer> primes) {
        HashMap<Integer, Integer> result = new HashMap<Integer, Integer>();

        while (x > 1) {
            for (int prime : primes) {
                if (x % prime != 0) {
                    continue;
                }

                if (result.containsKey(prime)) {
                    int count = result.get(prime) + 1;
                    result.put(prime, count);
                } else {
                    result.put(prime, 1);
                }

                x /= prime;

                if (x == 1) {
                    break;
                }
            }
        }

        return result;
    }

    /**
     * Returns all prime numbers less than the given number
     * 
     * @param max
     * @return
     */
    private static List<Integer> getPrimesLessThan(int max) {
        List<Integer> result = new ArrayList<Integer>();
        result.add(2);
        int num = 3;

        while (num < max) {
            if (isPrime(num, result)) {
                result.add(num);
            }

            num += 2;
        }

        return result;
    }

    private static boolean isPrime(int num, Collection<Integer> primes) {
        double cutOff = Math.sqrt(num);

        for (Integer prime : primes) {
            if (prime > cutOff) {
                break;
            } else if (num % prime == 0) {
                return false;
            }
        }

        return true;
    }
}
