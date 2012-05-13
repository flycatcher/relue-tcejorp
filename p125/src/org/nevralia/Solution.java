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
import java.util.HashSet;
import java.util.List;
import java.util.Set;

public class Solution {

    public static void main(String[] args) {
        final double threshold = 1e8;
        final int maxBase = (int) Math.round(Math.sqrt(threshold));
        List<Long> squares = new ArrayList<Long>(maxBase);

        for (long i = 1L; i <= maxBase; i++) {
            squares.add(i * i);
        }

        Set<Long> numbers = new HashSet<Long>();

        for (int length = 2; length <= squares.size(); length++) {
            long sum = 0;

            for (int i = 0; i < length; i++) {
                sum += squares.get(i);
            }

            if (sum >= threshold) {
                break;
            }

            for (int i = 0; i < squares.size() - length + 1; i++) {
                if (isPalindrome(sum)) {
                    numbers.add(sum);
                }

                if (i + length < squares.size()) {
                    sum -= squares.get(i);
                    sum += squares.get(i + length);
                }

                if (sum >= threshold) {
                    break;
                }
            }
        }

        long result = 0;

        for (long x : numbers) {
            result += x;
        }

        System.out.println(result);
    }

    private static boolean isPalindrome(long x) {
        List<Byte> digits = new ArrayList<Byte>();

        do {
            byte digit = (byte) (x % 10);
            x /= 10;
            digits.add(digit);
        } while (x > 0);

        int length = digits.size();

        if (length == 1) {
            return true;
        }

        int mid = length / 2;

        for (int i = 0; i < mid; i++) {
            byte a = digits.get(i);
            byte b = digits.get(length - i - 1);

            if (a != b) {
                return false;
            }
        }

        return true;
    }
}
