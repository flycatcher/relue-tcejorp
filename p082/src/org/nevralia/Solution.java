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

import java.io.BufferedReader;
import java.io.File;
import java.io.FileInputStream;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.List;

public class Solution {

    public static void main(String[] args) {
        List<List<Integer>> matrix = readFile(new File(args[0]));
        final int height = matrix.size();

        for (int column = matrix.get(0).size() - 2; column >= 0; column--) {
            List<Integer> costs = new ArrayList<Integer>(height);

            for (int row = 0; row < height; row++) {
                costs.add(matrix.get(row).get(column));
            }

            for (int rowToStart = 0; rowToStart < height; rowToStart++) {
                int minCosts = Integer.MAX_VALUE;

                for (int rowToProgress = 0; rowToProgress < height; rowToProgress++) {
                    int fromIndex = Math.min(rowToStart, rowToProgress);
                    int toIndex = Math.max(rowToStart, rowToProgress) + 1;
                    int total = matrix.get(rowToProgress).get(column + 1);

                    for (int cost : costs.subList(fromIndex, toIndex)) {
                        total += cost;
                    }

                    if (total < minCosts) {
                        minCosts = total;
                    }
                }

                matrix.get(rowToStart).set(column, minCosts);
            }
        }

        int result = Integer.MAX_VALUE;

        for (List<Integer> row : matrix) {
            if (row.get(0) < result) {
                result = row.get(0);
            }
        }

        System.out.println(result);
    }

    private static List<List<Integer>> readFile(final File file) {
        List<List<Integer>> result = new ArrayList<List<Integer>>();

        try {
            FileInputStream stream = new FileInputStream(file);
            InputStreamReader isr = new InputStreamReader(stream);
            BufferedReader reader = new BufferedReader(isr);

            String line;
            while ((line = reader.readLine()) != null) {
                String[] tokens = line.split(",");
                List<Integer> numbers = new ArrayList<Integer>(tokens.length);

                for (String token : tokens) {
                    int x = Integer.parseInt(token);
                    numbers.add(x);
                }

                result.add(numbers);
            }

        } catch (Exception e) {
            e.printStackTrace();
            System.exit(1);
        }

        return result;
    }
}
