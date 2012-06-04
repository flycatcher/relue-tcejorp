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
 * OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
 * SOFTWARE.
 */
var ans = (function(n, repeat) {

    function Dice(quantity, type) {
        this.quantity_ = quantity;
        this.type_ = type;
    }

    Dice.prototype.roll = function() {
        var result = [];
        for (var n = 0; n < this.quantity_; n++) {
            result.push(Math.floor(Math.random() * this.type_) + 1);
        }
        return result;
    };

    function Monopoly() {
        this.board_ = new Array();
        for (var i = 0; i < 40; i++) {
            this.board_.push(0);
        }
        this.position_ = 0;
        this.rolls_ = new Array();
    }

    Monopoly.prototype.popular = function() {
        var result = []
        for (var i = 0; i < this.board_.length; i++) {
            result.push(i);
        }
        var self = this;
        result.sort(function(a, b) {
            return (self.board_[b] - self.board_[a]);
        });
        return result.slice(0, 3).join();
    };

    Monopoly.prototype.doubles = function() {
        var result = this.rolls_.reduce(function(accu, curr) {
            return (curr[0] === curr[1]) ? accu + 1 : accu;
        }, 0);
        return result;
    };

    Monopoly.prototype.move = function(rolls) {
        this.rolls_.shift();
        this.rolls_.push(rolls);
        if (this.doubles() === 3) {
            // 3 doubles => Jail
            this.position_ = 10;
            this.board_[this.position_] += 1;
            this.rolls_.length = 0;
            return true;
        }
        this.position_ = (this.position_ + rolls[0] + rolls[1]) % 40;
        if (this.position_ === 30) {
            // Go to Jail => Jail
            this.position_ = 10;
        } else if (this.position_ === 7 || this.position_ === 22 || this.position_ === 36) {
            var ch = Math.floor(Math.random() * 16)
            if (ch === 0) {
                // Advance to Go
                this.position_ = 0;
            } else if (ch === 1) {
                // Go to Jail
                this.position_ = 10;
            } else if (ch === 2) {
                // Go to C1
                this.position_ = 11;
            } else if (ch === 3) {
                // Go to E3
                this.position_ = 24;
            } else if (ch === 4) {
                // Go to H2
                this.position_ = 39;
            } else if (ch === 5) {
                // Go to R1
                this.position_ = 5;
            } else if (ch === 6 || ch === 7) {
                // Go to next R
                if (this.position_ === 7) {
                    // CH1 => R2
                    this.position_ = 15;
                } else if (this.position_ === 22) {
                    // CH2 => R3
                    this.position_ = 25;
                } else {
                    // CH3 => R1
                    this.position_ = 5;
                }
            } else if (ch === 8) {
                // Go to next U
                if (this.position_ === 7 || this.position_ === 36) {
                    // CH1, CH3 => U1
                    this.position_ = 12;
                } else {
                    // CH2 => U2
                    this.position_ = 28;
                }
            } else if (ch === 9) {
                // Go back 3 squares
                this.position_ -= 3;
            }
        } else if (this.position_ === 2 || this.position_ === 17 || this.position_ === 33) {
            var cc = Math.floor(Math.random() * 16);
            if (cc === 0) {
                // Advance to Go
                this.position_ = 0;
            } else if (cc === 1) {
                // Go to Jail
                this.position_ = 10;
            }
        }
        this.board_[this.position_] += 1;
        return true;
    };

    var dice = new Dice(2, n);
    var game = new Monopoly();
    for (var i = 0; i < repeat; i++) {
        game.move(dice.roll());
    }

    return game.popular();
})(4, 1000000);

console.log(ans);