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
import java.util.Collection;
import java.util.HashMap;
import java.util.HashSet;
import java.util.List;
import java.util.Map;
import java.util.Set;

public class Solution {

    public static void main(String[] args) {
        final int MAX_NUMBER = 1 << 27;
        Collection<Integer> primes = sievePrimes(MAX_NUMBER);
        Map<Integer, Set<Integer>> affinityMap = analyze(primes);
        Collection<Set<Integer>> cliques = findCliquesOfSize(affinityMap, 5);

        for (Set<Integer> clique : cliques) {
            int sum = 0;
            System.out.print("{ ");
            for (int x : clique) {
                sum += x;
                System.out.print(x);
                System.out.print(" ");
            }
            System.out.print("} ");
            System.out.println(sum);
        }
    }

    private static Collection<Set<Integer>> findCliquesOfSize(
        Map<Integer, Set<Integer>> affinityMap, int size) {
        Collection<Set<Integer>> result = new HashSet<>();

        for (Map.Entry<Integer, Set<Integer>> entry : affinityMap.entrySet()) {
            int p1 = entry.getKey();
            for (int p2 : entry.getValue()) {
                Set<Integer> clique = new HashSet<>(Arrays.asList(p1, p2));
                result.add(clique);
            }
        }

        for (int cliqueSize = 3; cliqueSize <= size; cliqueSize++) {
            Set<Integer> primes = new HashSet<>();
            for (Set<Integer> clique : result) {
                primes.addAll(clique);
            }

            List<Set<Integer>> toBeAdded = new ArrayList<>();

            for (int prime : primes) {
                Set<Integer> affinity = affinityMap.get(prime);

                for (Set<Integer> clique : result) {
                    if (clique.contains(prime)) {
                        continue;
                    }

                    if (affinity.containsAll(clique)) {
                        Set<Integer> clone = new HashSet<>(clique);
                        clone.add(prime);
                        toBeAdded.add(clone);
                    }
                }
            }

            result.clear();
            result.addAll(toBeAdded);
        }

        return result;
    }

    private static Map<Integer, Set<Integer>> analyze(Collection<Integer> primes) {
        HashMap<Integer, Set<Integer>> result = new HashMap<>();

        for (int prime : primes) {
            String str = Integer.toString(prime);

            if (str.length() == 1) {
                continue;
            }

            for (int i = 1, size = str.length(); i < size; i++) {
                String prefix = str.substring(0, i);
                String suffix = str.substring(i);

                if (suffix.charAt(0) == '0') {
                    continue;
                }

                int front = Integer.parseInt(prefix);
                int back = Integer.parseInt(suffix);
                int number = Integer.parseInt(suffix + prefix);

                if (primes.contains(front) == false)
                    continue;
                if (primes.contains(back) == false)
                    continue;
                if (primes.contains(number) == false)
                    continue;

                if (result.containsKey(front) == false)
                    result.put(front, new HashSet<Integer>());
                if (result.containsKey(back) == false)
                    result.put(back, new HashSet<Integer>());

                result.get(front).add(back);
                result.get(back).add(front);
            }
        }

        return result;
    }

    /**
     * Returns a collection of all distinct prime numbers less than the given
     * number
     * 
     * @param maxNumber
     * @return
     */
    private static Collection<Integer> sievePrimes(final int maxNumber) {
        boolean[] sieve = new boolean[maxNumber];
        Arrays.fill(sieve, true);

        for (int i = 3; i < sieve.length; i += 2) {
            if (sieve[i] == true) {
                for (int j = 2 * i; j < sieve.length; j += i) {
                    sieve[j] = false;
                }
            }
        }

        Set<Integer> result = new HashSet<>();

        if (maxNumber > 2) {
            result.add(2);
        }

        for (int i = 3; i < sieve.length; i += 2) {
            if (sieve[i]) {
                result.add(i);
            }
        }

        return result;
    }
}
