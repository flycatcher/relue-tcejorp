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
     * A point in a plane
     * 
     * @constructor
     * @param {number}
     *            x The x-coordinate
     * @param {number}
     *            y The y-coordinate
     */
    function Point(x, y) {
        this.x_ = x;
        this.y_ = y;
    }

    Point.prototype = {
        constructor : Point,
        x : function(v) {
            if (v !== undefined && typeof v === "number") {
                this.x_ = v;
            }
            return this.x_;
        },
        y : function(v) {
            if (v !== undefined && typeof v === "number") {
                this.y_ = v;
            }
            return this.y_;
        },
        toString : function() {
            return "(" + this.x_ + ", " + this.y_ + ")";
        }
    };

    module.exports = Point;
})();