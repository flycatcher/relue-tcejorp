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
 * 
 * References:
 * 
 * 1. http://mathworld.wolfram.com/SternsDiatomicSeries.html
 */
package org.nevralia;

import java.math.BigInteger;
import java.util.HashMap;
import java.util.Map;

public class Solution {

    private static Map<BigInteger, Long> sternsTable = new HashMap<>();

    public static void main(String[] args) {
        final BigInteger n = BigInteger.TEN.pow(25).add(BigInteger.ONE);
        long ans = sterns(n);
        System.out.println(ans);
    }

    /**
     * Returns the nth term of Stern's diatomic sequence
     * 
     * @param n
     * @return
     */
    private static long sterns(BigInteger n) {
        if (BigInteger.ZERO.equals(n))
            return 0L;
        if (BigInteger.ONE.equals(n))
            return 1L;
        if (sternsTable.containsKey(n))
            return sternsTable.get(n);

        int k = n.getLowestSetBit();
        if (k > 0) {
            n = n.shiftRight(k);
        }
        
        BigInteger m = n.shiftRight(1);
        long result = sterns(m) + sterns(m.add(BigInteger.ONE));
        sternsTable.put(n, result);

        return result;
    }
}
