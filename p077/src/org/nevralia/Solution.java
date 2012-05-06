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
import java.util.HashSet;
import java.util.List;
import java.util.Map;

public class Solution {

    /**
     * It is possible to write ten as the sum of primes in exactly five
     * different ways:
     * 
     * 7 + 3 5 + 5 5 + 3 + 2 3 + 3 + 2 + 2 2 + 2 + 2 + 2 + 2
     * 
     * What is the first value which can be written as the sum of primes in over
     * five thousand different ways?
     * 
     * @param args
     */
    public static void main(String[] args) {
        int maxNum = 80;
        int maxUnits = maxNum / 2;
        List<Integer> bases = getPrimesLessThan(maxNum);
        Map<Integer, Integer> masterSheet = new HashMap<Integer, Integer>();
        Collection<Combo> previousCombos = new HashSet<Combo>();

        for (Integer base : bases) {
            Combo combo = new Combo();
            combo.put(base, 1);
            previousCombos.add(combo);
            masterSheet.put(combo.getSum(), 1);
        }

        for (int i = 2; i <= maxUnits; i++) {
            Collection<Combo> stageCombos = new HashSet<Combo>();

            for (Combo combo : previousCombos) {
                for (Integer base : bases) {
                    Combo clone = combo.clone();

                    if (clone.containsKey(base)) {
                        int units = clone.get(base) + 1;
                        clone.put(base, units);
                    } else {
                        clone.put(base, 1);
                    }

                    int sum = clone.getSum();

                    if (sum > maxNum) {
                        continue;
                    } else if (stageCombos.contains(clone)) {
                        continue;
                    }

                    stageCombos.add(clone);

                    if (masterSheet.containsKey(sum)) {
                        int numCombos = masterSheet.get(sum) + 1;
                        masterSheet.put(sum, numCombos);
                    } else {
                        masterSheet.put(sum, 1);
                    }
                }
            }

            previousCombos = stageCombos;
        }

        for (Map.Entry<Integer, Integer> entry : masterSheet.entrySet()) {
            if (entry.getValue() > 4500) {
                System.out.printf("%d : %d\n", entry.getKey(), entry.getValue());
            }
        }
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
