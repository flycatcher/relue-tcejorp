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

import java.util.HashMap;
import java.util.Map;

@SuppressWarnings("serial")
public class Combo extends HashMap<Integer, Integer> {

    public Combo() {
        // TODO Auto-generated constructor stub
    }

    public Combo(int initialCapacity) {
        super(initialCapacity);
        // TODO Auto-generated constructor stub
    }

    public Combo(Map<? extends Integer, ? extends Integer> m) {
        super(m);
        // TODO Auto-generated constructor stub
    }

    public Combo(int initialCapacity, float loadFactor) {
        super(initialCapacity, loadFactor);
        // TODO Auto-generated constructor stub
    }

    @Override
    public Combo clone() {
        Combo result = new Combo(this.size());

        for (Map.Entry<Integer, Integer> entry : this.entrySet()) {
            result.put(entry.getKey(), entry.getValue());
        }

        return result;
    }

    /**
     * Returns the numeric sum that this combination represents
     * 
     * @return
     */
    public int getSum() {
        int result = 0;

        for (Map.Entry<Integer, Integer> entry : this.entrySet()) {
            result += entry.getKey() * entry.getValue();
        }

        return result;
    }
}
