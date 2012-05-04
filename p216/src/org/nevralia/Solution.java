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
import java.util.List;

public class Solution {

    public static void main(String[] args) {
        final int maxN = 50000000;
        List<Long> candidates = new ArrayList<Long>(maxN + 1);

        for (long n = 0; n <= maxN; n++) {
            candidates.add(2L * n * n - 1L);
        }

        for (int n = 2, size = candidates.size(); n < size; n++) {
            long p = candidates.get(n);

            if (p < 2L || p > size * 2) {
                continue;
            }

            for (int m = n + (int) p; m < size; m += (int) p) {
                long candidate = candidates.get(m);
                while (candidate % p == 0) {
                    candidate /= p;
                }
                candidates.set(m, candidate);
            }

            for (int m = (int) p - n; m < size; m += (int) p) {
                long candidate = candidates.get(m);
                while (candidate % p == 0) {
                    candidate /= p;
                }
                candidates.set(m, candidate);
            }
        }

        int result = 0;

        for (int n = 2; n <= maxN; n++) {
            if (candidates.get(n) == 2L * n * n - 1L) {
                result += 1;
            }
        }

        System.out.println(result);
    }
}
