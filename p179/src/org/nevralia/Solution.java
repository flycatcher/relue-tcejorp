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
        final int max = 10000000;
        List<Integer> divisors = new ArrayList<Integer>(max);

        for (int i = 0; i < max; i++) {
            divisors.add(0);
        }

        for (int i = 1; i < divisors.size(); i++) {
            for (int j = i; j < divisors.size(); j += i) {
                int num = divisors.get(j) + 1;
                divisors.set(j, num);
            }
        }

        int result = 0;

        for (int i = 1; i < divisors.size() - 1; i++) {
            if (divisors.get(i) == divisors.get(i + 1)) {
                result += 1;
            }
        }

        System.out.println(result);
    }

}
