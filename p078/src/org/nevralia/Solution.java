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
        final long million = 1000000L;
        final int max = 100001;

        List<Long> partitions = new ArrayList<Long>(max);
        partitions.add(1L);

        for (int numCoins = 1; numCoins < max; numCoins++) {
            long numPartition = 0L;
            int i = 1, m = 1;

            while (i > 0) {
                i = numCoins - (3 * m * m + m) / 2;

                if (i >= 0) {
                    numPartition = (m % 2 == 0)
                            ? numPartition - partitions.get(i)
                            : numPartition + partitions.get(i);
                }

                i = numCoins - (3 * m * m - m) / 2;

                if (i >= 0) {
                    numPartition = (m % 2 == 0)
                            ? numPartition - partitions.get(i)
                            : numPartition + partitions.get(i);
                }

                m += 1;
            }

            numPartition %= million;

            if (numPartition == 0L) {
                System.out.println(numCoins);
                System.exit(0);
            }

            partitions.add(numPartition);
        }
    }
}
