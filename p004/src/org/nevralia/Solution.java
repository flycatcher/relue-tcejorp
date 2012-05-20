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
        int result = 0;

        for (int i = 999; i >= 100; --i) {
            for (int j = i; j >= 100; --j) {
                int number = i * j;

                if (number > result && isPalindrome(number)) {
                    result = number;
                }
            }
        }

        System.out.println(result);
    }

    private static boolean isPalindrome(int number) {
        List<Byte> digits = new ArrayList<Byte>();

        while (number > 0) {
            digits.add((byte) (number % 10));
            number /= 10;
        }

        int length = digits.size();

        for (int i = 0; i < length / 2; i++) {
            byte head = digits.get(i);
            byte tail = digits.get(length - i - 1);

            if (head != tail) {
                return false;
            }
        }

        return true;
    }

}
