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
 * 
 * References:
 * 
 * 1. Warren, Henry S. Hacker's Delight. Sec. 11.3 Integer Exponentiation.
 * Boston: Addison Wesley Professional, 2002 (ISBN 0201914654)
 */
var ans = (function(a, b) {
    function State(n, an) {
        this.power_ = n;
        this.ancestors_ = an;
    }

    State.prototype.exp = function() {
        return this.power_;
    };

    State.prototype.depth = function() {
        return this.ancestors_.length;
    };

    State.prototype.successors = function() {
        var p = this.power_;
        var a = this.ancestors_.slice(0);
        if (a.indexOf(p) < 0) {
            a.push(p);
            a.sort(function(x, y) {
                return x - y;
            });
        }
        var result = a.map(function(m) {
            return new State(p + m, a);
        });
        return result;
    };

    function ExpTools() {}

    ExpTools.prototype.search = function(n) {
        var o = [new State(1, [])];
        var closed = {};
        while (true) {
            var state = o.shift();
            var e = state.exp();
            if (e === n) {
                return state.depth();
            }
            closed[e] = true;
            state.successors().forEach(function(x) {
                if ((x.exp() in closed) === false) {
                    o.push(x);
                }
            });
        }
        return -1;
    };

    var expTools = new ExpTools();
    var i, result = 0;
    for (i = a; i <= b; i++) {
        result += expTools.search(i);
    }
    return result;
})(1, 200);

console.log(ans);