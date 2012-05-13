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

import java.io.File;
import java.io.FileNotFoundException;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collection;
import java.util.HashMap;
import java.util.HashSet;
import java.util.List;
import java.util.Map;
import java.util.PriorityQueue;
import java.util.Queue;
import java.util.Scanner;
import java.util.Set;

public class Solution {

    public static void main(String[] args) {
        int[][] costs = read(new File(args[0]));
        Map<List<Integer>, Node> unvisited = init(costs.length);
        Node start = unvisited.get(Arrays.asList(0, 0));
        start.setCost(costs[0][0]);
        Set<Node> open = new HashSet<Node>();
        open.add(start);

        while (open.isEmpty() == false) {
            Queue<Node> frontier = new PriorityQueue<Node>(open);
            Node node = frontier.poll();
            open.remove(node);
            List<Integer> coordinate = node.getIdentity();
            unvisited.remove(coordinate);
            int row = coordinate.get(0);
            int col = coordinate.get(1);

            if (row == col && col == costs.length - 1) {
                System.out.println(node.getCost());
                System.exit(0);
            }

            Collection<Node> successors = neighbors(node, unvisited);
            open.addAll(successors);

            for (Node successor : successors) {
                coordinate = successor.getIdentity();
                row = coordinate.get(0);
                col = coordinate.get(1);

                int cost = costs[row][col] + node.getCost();

                if (successor.getCost() > cost) {
                    successor.setCost(cost);
                }
            }
        }
    }

    private static Collection<Node> neighbors(Node self, Map<List<Integer>, Node> nodes) {
        List<Integer> coordinate = self.getIdentity();
        int row = coordinate.get(0);
        int col = coordinate.get(1);

        List<Node> result = new ArrayList<Node>(4);

        List<Integer> left = Arrays.asList(row, col - 1);
        if (nodes.containsKey(left)) {
            result.add(nodes.get(left));
        }

        List<Integer> down = Arrays.asList(row + 1, col);
        if (nodes.containsKey(down)) {
            result.add(nodes.get(down));
        }

        List<Integer> right = Arrays.asList(row, col + 1);
        if (nodes.containsKey(right)) {
            result.add(nodes.get(right));
        }

        List<Integer> up = Arrays.asList(row - 1, col);
        if (nodes.containsKey(up)) {
            result.add(nodes.get(up));
        }

        return result;
    }

    private static Map<List<Integer>, Node> init(int dimension) {
        Map<List<Integer>, Node> result = new HashMap<List<Integer>, Node>(dimension * dimension);

        for (int row = 0; row < dimension; row++) {
            for (int col = 0; col < dimension; col++) {
                Node node = new Node(row, col);
                result.put(node.getIdentity(), node);
            }
        }

        return result;
    }

    private static int[][] read(File file) {
        List<String> lines = new ArrayList<String>();

        try {
            Scanner scanner = new Scanner(file);
            while (scanner.hasNextLine()) {
                String line = scanner.nextLine();
                lines.add(line);
            }
        } catch (FileNotFoundException e) {
            e.printStackTrace();
            System.exit(1);
        }

        int height = lines.size();
        int[][] result = new int[height][height];

        for (int i = 0; i < height; i++) {
            String line = lines.get(i);
            String[] tokens = line.split(",+", height);
            for (int j = 0; j < tokens.length; j++) {
                int x = Integer.parseInt(tokens[j]);
                result[i][j] = x;
            }
        }

        return result;
    }
}
