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

@SuppressWarnings("serial")
public class Envelope extends HashMap<Paper, Integer> {
    private double probability_;

    public double getProbability() {
        return probability_;
    }

    public void setProbability(double value) {
        this.probability_ = value;
    }

    /**
     * Returns a deep copy of this instance
     * 
     * @return
     */
    private Envelope copy() {
        Envelope clone = new Envelope();
        for (Map.Entry<Paper, Integer> entry : this.entrySet()) {
            clone.put(entry.getKey(), entry.getValue());
        }
        clone.setProbability(this.getProbability());
        return clone;
    }

    private int total() {
        int total = 0;
        total += this.get(Paper.A2);
        total += this.get(Paper.A3);
        total += this.get(Paper.A4);
        total += this.get(Paper.A5);
        return total;
    }
    
    public int singles() {
        int result = 0;
        result += this.get(Paper.SA2);
        result += this.get(Paper.SA3);
        result += this.get(Paper.SA4);
        return result;
    }

    public List<Envelope> nextBatch() {
        List<Envelope> result = new ArrayList<>();
        int total = this.total();
        double prop = this.getProbability() / total;

        if (this.get(Paper.A2) > 0) {
            Envelope clone = this.copy();
            clone.setProbability(prop * clone.get(Paper.A2));
            clone.put(Paper.A2, clone.get(Paper.A2) - 1);
            clone.put(Paper.A3, clone.get(Paper.A3) + 1);
            clone.put(Paper.A4, clone.get(Paper.A4) + 1);
            clone.put(Paper.A5, clone.get(Paper.A5) + 1);
            result.add(clone);
        }

        if (this.get(Paper.A3) > 0) {
            Envelope clone = this.copy();
            clone.setProbability(prop * clone.get(Paper.A3));
            clone.put(Paper.A3, clone.get(Paper.A3) - 1);
            clone.put(Paper.A4, clone.get(Paper.A4) + 1);
            clone.put(Paper.A5, clone.get(Paper.A5) + 1);
            result.add(clone);
        }

        if (this.get(Paper.A4) > 0) {
            Envelope clone = this.copy();
            clone.setProbability(prop * clone.get(Paper.A4));
            clone.put(Paper.A4, clone.get(Paper.A4) - 1);
            clone.put(Paper.A5, clone.get(Paper.A5) + 1);
            result.add(clone);
        }

        if (this.get(Paper.A5) > 0) {
            Envelope clone = this.copy();
            clone.setProbability(prop * clone.get(Paper.A5));
            clone.put(Paper.A5, clone.get(Paper.A5) - 1);
            if (clone.total() == 1) {
                if (clone.get(Paper.A2) == 1) {
                    clone.put(Paper.SA2, 1);
                } else if (clone.get(Paper.A3) == 1) {
                    clone.put(Paper.SA3, 1);
                } else if (clone.get(Paper.A4) == 1) {
                    clone.put(Paper.SA4, 1);
                }
            }
            result.add(clone);
        }

        return result;
    }
}
