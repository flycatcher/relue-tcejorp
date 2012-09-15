/**
 * @license Copyright (C) 2012, Jun Mei
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
(function() {
    var util = require("util");
    var BinarySearchTree = require("./BinarySearchTree");

    var tree = new BinarySearchTree(function(x, y) {
        return (x - y);
    });

    // Test insert
    tree.insert(1);
    console.log("Insert 1");
    console.log(util.format("size: %d", tree.size()));
    console.log(util.format("min: %d", tree.min()));
    console.log(util.format("max: %d", tree.max()));
    tree.print();

    tree.insert(2);
    console.log("Insert 2");
    tree.print();

    tree.insert(-100);
    console.log("Insert -100");
    tree.print();

    // Test inserting existing value
    tree.insert(-100);
    console.log("Insert -100");
    console.log(util.format("size: %d", tree.size()));
    console.log(util.format("min: %d", tree.min()));
    console.log(util.format("max: %d", tree.max()));

    // Test removing a value
    tree.remove(-100);
    console.log("Remove -100");
    console.log(util.format("size: %d", tree.size()));
    console.log(util.format("min: %d", tree.min()));
    console.log(util.format("max: %d", tree.max()));
    tree.print();

    console.log("Insert 10 random numbers");
    var step = 0;
    for (step = 0; step < 10; step++) {
        tree.insert(Math.floor(Math.random() * 10 - 5));
    }
    tree.print();

    while (tree.size() > 0) {
        var n = tree.max();
        console.log(util.format("Remove max %d", n));
        tree.remove(n);
        tree.print();
    }

    console.log("Insert 10 random numbers");
    var step = 0;
    for (step = 0; step < 10; step++) {
        tree.insert(Math.floor(Math.random() * 10 - 5));
    }
    tree.print();

    while (tree.size() > 0) {
        var n = tree.min();
        console.log(util.format("Remove min %d", n));
        tree.remove(n);
        tree.print();
    }
})();