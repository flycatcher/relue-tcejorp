/**
 * Copyright (C) 2012, Jun Mei
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
package nevralia;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collection;
import java.util.HashMap;
import java.util.LinkedList;
import java.util.List;
import java.util.Map;

public class Solution {

    public static void main(String[] args) {
        long ans = count(17, 3);
        System.out.println(ans);
    }

    private static long count(int numDigits, final int repeats) {
        Map<List<Integer>, Long> oTracker = initCounters();
        while (numDigits > 0) {
            Map<List<Integer>, Long> nTracker = new HashMap<>();
            for (Map.Entry<List<Integer>, Long> entry : oTracker.entrySet()) {
                Collection<List<Integer>> children = successors(entry.getKey(),
                    repeats);
                for (List<Integer> lst : children) {
                    if (nTracker.containsKey(lst)) {
                        long x = entry.getValue() + nTracker.get(lst);
                        nTracker.put(lst, x);
                    } else {
                        nTracker.put(lst, entry.getValue());
                    }
                }
            }
            oTracker = nTracker;
            numDigits -= 1;
        }
        long result = 0;
        for (long x : oTracker.values()) {
            result += x;
        }
        return result;
    }

    private static Collection<List<Integer>> successors(List<Integer> lst,
        final int repeats) {
        Collection<List<Integer>> result = new LinkedList<>();
        for (int n = 0; n < 10; n++) {
            int x = lst.get(n);
            if (x < repeats) {
                List<Integer> child = new ArrayList<>();
                child.addAll(lst);
                child.set(n, x + 1);
                result.add(child);
            }
        }
        return result;
    }

    private static Map<List<Integer>, Long> initCounters() {
        Map<List<Integer>, Long> result = new HashMap<>();
        for (int n = 1; n < 10; n++) {
            List<Integer> key = Arrays.asList(0, 0, 0, 0, 0, 0, 0, 0, 0, 0);
            key.set(n, 1);
            result.put(key, 1L);
        }
        return result;
    }

}
