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
import java.util.Collections;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class Solution {

    public static void main(String[] args) {
        final int upperBound = 10000;
        Map<String, List<Integer>> primeFamilies = new HashMap<String, List<Integer>>();
        for (int prime : getPrimesLessThan(upperBound)) {
            if (prime > (upperBound / 10)) {
                String sig = getSignature(prime);
                if (primeFamilies.containsKey(sig) == false) {
                    primeFamilies.put(sig, new ArrayList<Integer>());
                }
                primeFamilies.get(sig).add(prime);
            }
        }

        for (List<Integer> family : primeFamilies.values()) {
            if (family.size() < 3) {
                continue;
            }

            for (int i = 0; i < family.size() - 2; i++) {
                int p1 = family.get(i);
                for (int j = i + 2; j < family.size(); j++) {
                    int p3 = family.get(j);
                    int p2 = (p1 + p3) >> 1;
                    if (Collections.binarySearch(family, p2) >= 0) {
                        System.out.printf("%d %d %d\n", p1, p2, p3);
                    }
                }
            }
        }
    }

    private static String getSignature(final int number) {
        char[] digits = Integer.toString(number).toCharArray();
        Arrays.sort(digits);
        return new String(digits);
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
