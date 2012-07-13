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

import java.util.Collection;
import java.util.HashMap;
import java.util.Map;

public class Solution {

    public static void main(String[] args) {
        Map<PrizeNode, Long> pStage = initStage();
        int steps = 29;
        while (steps > 0) {
            Map<PrizeNode, Long> nStage = new HashMap<>();
            for (Map.Entry<PrizeNode, Long> entry : pStage.entrySet()) {
                Collection<PrizeNode> nodes = entry.getKey().getSuccessors();
                for (PrizeNode node : nodes) {
                    if (nStage.containsKey(node) == false) {
                        nStage.put(node, entry.getValue());
                    } else {
                        long x = nStage.get(node) + entry.getValue();
                        nStage.put(node, x);
                    }
                }
            }
            pStage = nStage;
            steps -= 1;
        }
        long ans = 0L;
        for (long x : pStage.values()) {
            ans += x;
        }
        System.out.println(ans);
    }

    private static Map<PrizeNode, Long> initStage() {
        Map<PrizeNode, Long> result = new HashMap<>();
        result.put(new PrizeNode(Attendance.Absent), 1L);
        result.put(new PrizeNode(Attendance.Late), 1L);
        result.put(new PrizeNode(Attendance.OnTime), 1L);
        return result;
    }

}
