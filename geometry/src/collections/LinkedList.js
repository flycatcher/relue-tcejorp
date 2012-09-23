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
     * Data container that represents an element in a doubly linked list
     * 
     * @constructor
     * @param {*} value
     */
    function ListNode(value) {
        this.value_ = value;
        this.next_ = null;
        this.prev_ = null;
    }

    ListNode.prototype = {
        constructor : ListNode,
        value : function(v) {
            if (v !== undefined) {
                this.value_ = v;
                return this;
            }
            return this.value_;
        },
        next : function(n) {
            if (n === null || n instanceof ListNode) {
                this.next_ = n;
                return this;
            }
            return this.next_;
        },
        prev : function(n) {
            if (n === null || n instanceof ListNode) {
                this.prev_ = n;
                return this;
            }
            return this.prev_;
        }
    };

    /**
     * Data container representing a doubly linked list
     * 
     * @constructor
     */
    function LinkedList() {
        this.head_ = null;
        this.tail_ = null;
        this.size_ = 0;
    }

    LinkedList.prototype = {
        constructor : LinkedList,
        size : function() {
            return this.size_;
        },
        addFirst : function(item) {
            var node = new ListNode(item);
            if (this.size_ === 0) {
                this.head_ = node;
                this.tail_ = node;
            } else {
                node.next(this.head_);
                this.head_.prev(node);
                this.head_ = node;
            }
            this.size_ += 1;
            return this;
        },
        addLast : function(item) {
            var node = new ListNode(item);
            if (this.size_ === 0) {
                this.head_ = node;
                this.tail_ = node;
            } else {
                node.prev(this.tail_);
                this.tail_.next(node);
                this.tail_ = node;
            }
            this.size_ += 1;
            return this;
        },
        removeFirst : function() {
            if (this.size_ === 0) {
                return null;
            }
            var node = this.head_;
            if (this.size_ === 1) {
                this.head_ = null;
                this.tail_ = null;
            } else {
                this.head_ = node.next();
                this.head_.prev(null);
            }
            this.size_ -= 1;
            return node.value();
        },
        removeLast : function() {
            if (this.size_ === 0) {
                return null;
            }
            var node = this.tail_;
            if (this.size_ === 1) {
                this.head_ = null;
                this.tail_ = null;
            } else {
                this.tail_ = node.prev();
                this.tail_.next(null);
            }
            this.size_ -= 1;
            return node.value();
        },
        first : function() {
            return (this.head_) ? this.head_.value() : null;
        },
        last : function() {
            return (this.tail_) ? this.tail_.value() : null;
        }
    };

    module.exports = LinkedList;
})();