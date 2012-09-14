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
    /**
     * Data container representing a node in a binary tree
     * 
     * @constructor
     */
    function BinaryTreeNode() {
        this.value_ = undefined;
        this.left_ = undefined;
        this.right_ = undefined;
    }

    BinaryTreeNode.prototype = {
        constructor : BinaryTreeNode,
        value : function(v) {
            if (v !== undefined) {
                this.value_ = v;
            }
            return this.value_;
        },
        left : function(node) {
            if (node !== undefined && node instanceof BinaryTreeNode) {
                this.left_ = node;
            }
            return this.left_;
        },
        right : function(node) {
            if (node !== undefined && node instanceof BinaryTreeNode) {
                this.right_ = node;
            }
            return this.right_;
        }
    };

    module.exports = BinaryTreeNode;
})();