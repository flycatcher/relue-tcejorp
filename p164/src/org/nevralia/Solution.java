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

import java.util.Arrays;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class Solution {

    private static final int THRESHOLD = 9;

    public static void main(String[] args) {
        Map<List<Byte>, Long> currentStage = initStage(1L);

        for (int stage = 3; stage < 20; stage++) {
            currentStage = nextStage(currentStage);
        }

        long result = 0L;

        for (Map.Entry<List<Byte>, Long> entry : currentStage.entrySet()) {
            List<Byte> key = entry.getKey();
            int diff = THRESHOLD - key.get(0) - key.get(1);
            result += diff * entry.getValue();
        }

        System.out.println(result);
    }

    private static Map<List<Byte>, Long> nextStage(final Map<List<Byte>, Long> lastStage) {
        Map<List<Byte>, Long> result = initStage(0L);

        for (Map.Entry<List<Byte>, Long> entry : result.entrySet()) {
            List<Byte> digits = entry.getKey();
            byte first = digits.get(0), second = digits.get(1);
            int sum = first + second;
            long count = 0L;

            for (byte third = 0; third <= THRESHOLD - sum; third++) {
                List<Byte> key = Arrays.asList(second, third);
                count += lastStage.get(key);
            }

            entry.setValue(count);
        }

        return result;
    }

    private static Map<List<Byte>, Long> initStage(long defaultValue) {
        Map<List<Byte>, Long> result = new HashMap<List<Byte>, Long>();

        for (byte first = 0; first < 10; first++) {
            for (byte second = 0; second < 10; second++) {
                if (first + second <= THRESHOLD) {
                    result.put(Arrays.asList(first, second), defaultValue);
                } else {
                    break;
                }
            }
        }

        return result;
    }
}
