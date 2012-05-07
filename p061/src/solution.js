/**
 * @license Copyright (c) 2012, Jun Mei
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
 * OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
 * THE SOFTWARE.
 */
var ans = (function(n) {
    /**
     * Initializes a new polygonal number generator
     *
     * @constructor
     * @this {Generator}
     * @param {number} numOfDigits
     */
    function Generator(numOfDigits) {
        this.min_ = Math.pow(10, numOfDigits - 1);
        this.max_ = Math.pow(10, numOfDigits);
    }

    /**
     * Returns all triangle numbers of the given size
     *
     * @this {Generator}
     * @returns {Array.<number>}
     */
    Generator.prototype.triangle = function() {
        var inverse = function(x) {
                return Math.ceil((Math.sqrt(8 * x + 1) - 1) / 2);
            };
        var n_min = inverse(this.min_),
            n_max = inverse(this.max_);
        var result = [];
        for (var n = n_min; n < n_max; n++) {
            result.push((n * n + n) >> 1);
        }
        return result;
    }

    /**
     * Returns all square numbers of the given size
     *
     * @this {Generator}
     * @returns {Array.<number>}
     */
    Generator.prototype.square = function() {
        var inverse = function(x) {
                return Math.ceil(Math.sqrt(x));
            };
        var n_min = inverse(this.min_),
            n_max = inverse(this.max_);
        var result = [];
        for (var n = n_min; n < n_max; n++) {
            result.push(n * n);
        }
        return result;
    }

    /**
     * Returns all pentagonal numbers of the given size
     *
     * @this {Generator}
     * @returns {Array.<number>}
     */
    Generator.prototype.pentagonal = function() {
        var inverse = function(x) {
                return Math.ceil((Math.sqrt(24 * x) + 1) / 6);
            };
        var n_min = inverse(this.min_),
            n_max = inverse(this.max_);
        var result = [];
        for (var n = n_min; n < n_max; n++) {
            result.push((3 * n * n - n) >> 1);
        }
        return result;
    }

    /**
     * Returns all hexagonal numbers of the given size
     *
     * @this {Generator}
     * @returns {Array.<number>}
     */
    Generator.prototype.hexagonal = function() {
        var inverse = function(x) {
                return Math.ceil((Math.sqrt(8 * x + 1) + 1) / 4);
            };
        var n_min = inverse(this.min_),
            n_max = inverse(this.max_);
        var result = [];
        for (var n = n_min; n < n_max; n++) {
            result.push(2 * n * n - n);
        }
        return result;
    }

    /**
     * Returns all heptagonal numbers of the given size
     *
     * @this {Generator}
     * @returns {Array.<number>}
     */
    Generator.prototype.heptagonal = function() {
        var inverse = function(x) {
                return Math.ceil((Math.sqrt(40 * x + 9) + 3) / 10);
            };
        var n_min = inverse(this.min_),
            n_max = inverse(this.max_);
        var result = [];
        for (var n = n_min; n < n_max; n++) {
            result.push((5 * n * n - 3 * n) >> 1);
        }
        return result;
    }

    /**
     * Returns all octagonal numbers of the given size
     *
     * @this {Generator}
     * @returns {Array.<number>}
     */
    Generator.prototype.octagonal = function() {
        var inverse = function(x) {
                return Math.ceil((Math.sqrt(3 * x + 1) + 1) / 3);
            };
        var n_min = inverse(this.min_),
            n_max = inverse(this.max_);
        var result = [];
        for (var n = n_min; n < n_max; n++) {
            result.push(3 * n * n - 2 * n);
        }
        return result;
    }

    /**
     * Initializes a new number indexer
     *
     * @constructor
     * @this {Indexer}
     */
    function Indexer() {}

    /**
     * Groups the given array of number by their first 2 digits (decimal form)
     * and returns the map
     *
     * @this {Indexer}
     * @param {Array.<number>} numbers
     * @returns {Object.<string, Array.<number>>}
     */
    Indexer.prototype.index = function(numbers) {
        var result = {};
        for (var i in numbers) {
            var x = numbers[i];
            var prefix = x.toString().slice(0, 2);
            if (prefix in result) {
                result[prefix].push(x);
            } else {
                result[prefix] = [x];
            }
        }
        return result;
    }

    /**
     * Initializes a data object representing an open state
     *
     * @constructor
     * @this {State}
     */
    function State() {
        /**
         * Collection of all distinct polygonal types that this instance has
         * visited so far
         * @type {Array.<string>}
         * @private
         */
        this.types_ = [];
        /**
         * Collection of all polygonal numbers that this instance has acquired
         * @type {Array.<number>}
         * @private
         */
        this.numbers_ = [];
    }

    /**
     * @this {State}
     * @returns {Array.<string>}
     */
    State.prototype.getTypes = function() {
        return this.types_;
    }

    /**
     * @this {State}
     * @param {Array.<string>} value
     */
    State.prototype.setTypes = function(value) {
        this.types_ = value;
    }

    /**
     * @this {State}
     * @returns {Array.<number>}
     */
    State.prototype.getNumbers = function() {
        return this.numbers_;
    }

    /**
     * @this {State}
     * @param {Array.<number>}
     */
    State.prototype.setNumbers = function(value) {
        this.numbers_ = value;
    }

    /**
     * Returns a clone of this instance
     * @this {State}
     * @returns {State}
     */
    State.prototype.clone = function() {
        var result = new State();
        result.setTypes(this.types_.slice(0));
        result.setNumbers(this.numbers_.slice(0));
        return result;
    }

    var gen = new Generator(n);
    var idx = new Indexer();
    var numbers = {
        "4": idx.index(gen.square()),
        "5": idx.index(gen.pentagonal()),
        "6": idx.index(gen.hexagonal()),
        "7": idx.index(gen.heptagonal()),
        "8": idx.index(gen.octagonal())
    };

    /**
     * Collection of open states
     * @type {Array.<State>}
     */
    var states = [];

    gen.triangle().forEach(function(polygonal) {
        var frontier = new State();
        frontier.getTypes().push("3");
        frontier.getNumbers().push(polygonal);
        states.push(frontier);
    });

    for (var stage = 1; stage < 6; stage++) {
        var frontiers = [];

        for (var i in states) {
            var state = states[i];
            for (var type in numbers) {
                if (state.getTypes().indexOf(type) > -1) {
                    continue;
                }

                var front = state.getNumbers()[0];
                var suffix = front.toString().slice(2);
                var polygonals = numbers[type];

                if ((suffix in polygonals) === false) {
                    continue;
                }

                polygonals[suffix].forEach(function(polygonal) {
                    var frontier = state.clone();
                    frontier.getNumbers().unshift(polygonal);
                    frontier.getTypes().unshift(type);
                    frontiers.push(frontier);
                });
            }
        }

        states = frontiers;
    }

    var result = 0;

    states.some(function(state) {
        var polygonals = state.getNumbers();
        polygonals.reverse();
        var list = polygonals.slice(0);
        var head = list.shift(),
            tail = list.pop();
        if (head.toString().slice(0, 2) === tail.toString().slice(2)) {
            console.log(polygonals);
            result = polygonals.reduce(function(total, value) {
                return total + value;
            }, 0);
            return true;
        }
        return false;
    });

    return result;
})(4);

console.log(ans);