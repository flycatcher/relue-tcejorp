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
import java.util.List;

public class Solution {

    public static void main(String[] args) {
        for (int i = 1; i < Integer.MAX_VALUE; i++) {
            if (isSameDigits(i)) {
                System.out.println(i);
                System.exit(0);
            }
        }
    }

    private static boolean isSameDigits(int number) {
        List<Integer> digits2 = getDigits(number * 2);
        int[] multipliers = { 3, 4, 5, 6 };

        for (int multiplier : multipliers) {
            List<Integer> digits = getDigits(number * multiplier);

            if (digits2.equals(digits) == false) {
                return false;
            }
        }

        return true;
    }

    private static List<Integer> getDigits(int number) {
        ArrayList<Integer> result = new ArrayList<Integer>();

        do {
            result.add(number % 10);
            number /= 10;
        } while (number > 0);

        Collections.sort(result);
        return result;
    }
}
