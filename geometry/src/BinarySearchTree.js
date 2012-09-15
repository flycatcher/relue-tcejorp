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
    var BinaryTreeNode = require("./BinaryTreeNode");

    /**
     * Data collection of a simple binary search tree
     * 
     * @constructor
     * @param {function(object,object):number}
     *            comparator
     */
    function BinarySearchTree(comparator) {
        this.root_ = null;
        this.size_ = 0;
        this.comparator_ = comparator;
    }

    BinarySearchTree.prototype = {
        constructor : BinarySearchTree,
        find : function(v) {
            var node = this.root_, result = false;
            while (node && !result) {
                var c = this.comparator_(v, node.value());
                if (c === 0) {
                    result = true;
                } else if (c < 0) {
                    node = node.left();
                } else {
                    node = node.right();
                }
            }
            return result;
        },
        insert : function(v) {
            var leaf = new BinaryTreeNode(v);
            if (!this.root_) {
                this.root_ = leaf;
                this.size_ += 1;
            } else {
                var node = this.root_;
                var c = this.comparator_(v, node.value());
                while ((c < 0 && node.left()) || (c > 0 && node.right())) {
                    node = (c < 0)
                        ? node.left()
                        : node.right();
                    c = this.comparator_(v, node.value());
                }
                if (c < 0 && !node.left()) {
                    node.left(leaf);
                    leaf.parent(node);
                    this.size_ += 1;
                } else if (c > 0 && !node.right()) {
                    node.right(leaf);
                    leaf.parent(node);
                    this.size_ += 1;
                }
            }
        },
        remove : function(v) {
            var node = this.root_, found = false;
            while (node && !found) {
                var c = this.comparator_(v, node.value());
                if (c === 0) {
                    found = true;
                } else if (c < 0) {
                    node = node.left();
                } else {
                    node = node.right();
                }
            }
            if (found) {
                var parent = node.parent(), replacement = null;

                if (node.left()) {
                    replacement = node.left();
                    while (replacement && replacement.right()) {
                        replacement = replacement.right();
                    }
                    if (replacement !== node.left()) {
                        node.value(replacement.value());
                        replacement.parent().right(replacement.left());
                        if (replacement.left()) {
                            replacement.left().parent(replacement.parent());
                        }
                    } else {
                        replacement.right(node.right());
                        replacement.parent(parent);
                        if (node.right()) {
                            node.right().parent(replacement);
                        }
                    }
                } else if (node.right()) {
                    replacement = node.right();
                    replacement.parent(parent);
                }

                if (replacement === node.right() || replacement === node.left()) {
                    if (!parent) {
                        this.root_ = replacement;
                    } else if (parent.left() === node) {
                        parent.left(replacement);
                    } else if (parent.right() === node) {
                        parent.right(replacement);
                    }
                }

                this.size_ -= 1;
            }
        },
        size : function() {
            return this.size_;
        },
        min : function() {
            var node = this.root_, result = undefined;
            while (node) {
                result = node.value();
                node = node.left();
            }
            return result;
        },
        max : function() {
            var node = this.root_, result = undefined;
            while (node) {
                result = node.value();
                node = node.right();
            }
            return result;
        },
        print : function() {
            var rprint = function(node) {
                if (node) {
                    rprint(node.left());
                    node.print();
                    rprint(node.right());
                }
            };

            if (this.root_) {
                rprint(this.root_);
            } else {
                console.log("Empty tree");
            }
        }
    };

    module.exports = BinarySearchTree;
})();