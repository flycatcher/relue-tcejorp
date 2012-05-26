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
import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class Solution {

    public static void main(String[] args) {
        Envelope envelope = new Envelope();
        // Initial state at the end of the first batch. With probability 1, we
        // have 1 piece of paper for A2, A3, A4, and A5 each.
        envelope.setProbability(1d);
        envelope.put(Paper.A2, 1);
        envelope.put(Paper.A3, 1);
        envelope.put(Paper.A4, 1);
        envelope.put(Paper.A5, 1);
        // Track whether or not we have previously processed an envelope with a
        // single sheet of paper with size A2, A3, or A4. None so far.
        envelope.put(Paper.SA2, 0);
        envelope.put(Paper.SA3, 0);
        envelope.put(Paper.SA4, 0);

        double exp = calculate(envelope, 14);
        System.out.println(exp);
    }

    /**
     * Returns the expected number of encountering a single-sheet envelope after
     * some number of iterations
     * 
     * @param initState
     * @param numIters
     * @return
     */
    private static double calculate(Envelope initState, int numIters) {
        // This collection maps each unique state to the probability of reaching
        // that state after each iteration.
        Map<Envelope, Double> envelopes = new HashMap<>();
        envelopes.put(initState, initState.getProbability());

        while (numIters > 0) {
            // This collection holds all successor states for the current
            // iteration. These states are not necessarily unique, so they will
            // be consolidated later.
            List<Envelope> successors = new ArrayList<>();

            for (Envelope envelope : envelopes.keySet()) {
                successors.addAll(envelope.nextBatch());
            }

            envelopes.clear();

            for (Envelope state : successors) {
                if (envelopes.containsKey(state)) {
                    double prop = envelopes.get(state) + state.getProbability();
                    state.setProbability(prop);
                    envelopes.remove(state);
                }
                envelopes.put(state, state.getProbability());
            }

            numIters -= 1;
        }

        double result = 0d;

        for (Envelope envelope : envelopes.keySet()) {
            result += envelope.getProbability() * envelope.singles();
        }

        return result;
    }
}
