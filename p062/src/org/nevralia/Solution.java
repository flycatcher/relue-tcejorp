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
import java.util.Collections;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class Solution {

    public static void main(String[] args) {
        Map<List<Byte>, List<Long>> cubes = new HashMap<List<Byte>, List<Long>>();
        final double max = Math.cbrt(Long.MAX_VALUE);

        for (long i = 0; i < max; i++) {
            long cube = i * i * i;
            List<Byte> signature = getSignature(cube);
            if (cubes.containsKey(signature)) {
                List<Long> family = cubes.get(signature);
                family.add(cube);

                if (family.size() >= 5) {
                    System.out.println(family.get(0));
                    System.exit(0);
                }
            } else {
                List<Long> family = new ArrayList<Long>();
                family.add(cube);
                cubes.put(signature, family);
            }
        }
    }

    private static List<Byte> getSignature(long number) {
        List<Byte> result = new ArrayList<Byte>();
        final byte ten = (byte) 10;

        do {
            byte r = (byte) (number % ten);
            result.add(r);
            number /= ten;
        } while (number > 0);

        Collections.sort(result);
        return result;
    }
}
