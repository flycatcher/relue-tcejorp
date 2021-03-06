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
        List<List<Integer>> nodes = readFile(new File(args[0]));

        for (int line = nodes.size() - 2; line >= 0; line--) {
            List<Integer> level = nodes.get(line);
            List<Integer> children = nodes.get(line + 1);

            for (int i = 0, size = level.size(); i < size; i++) {
                int leftChild = children.get(i);
                int rightChild = children.get(i + 1);
                int score = level.get(i) + Math.max(leftChild, rightChild);
                level.set(i, score);
            }
        }

        int result = nodes.get(0).get(0);
        System.out.println(result);
    }

    private static List<List<Integer>> readFile(File file) {
        List<List<Integer>> result = new ArrayList<List<Integer>>();

        try {
            FileInputStream stream = new FileInputStream(file);
            InputStreamReader isr = new InputStreamReader(stream);
            BufferedReader reader = new BufferedReader(isr);

            String line;
            while ((line = reader.readLine()) != null) {
                String[] tokens = line.split("\\s+");
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
