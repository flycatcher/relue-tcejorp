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
(function() {
    /**
     * @constructor
     */
    function ReverseReader(text) {
        this.text_ = (typeof text === "string")
            ? text
            : "";
        /**
         * An instance marker to indicate the reader's progress; in particular,
         * the substring from this index to the end has already been processed
         * 
         * @private
         * @type {number}
         */
        this.bookmark_ = this.text_.length;
        // Skip trailing spaces
        this.skipWhitespace_();
    }

    ReverseReader.prototype = {
        constructor : ReverseReader,
        hasNext : function() {
            return (this.bookmark_ > 0);
        },
        next : function() {
            if (this.bookmark_ <= 0) {
                return "";
            }
            var end = this.bookmark_;
            this.advanceBookmark_();
            var result = this.text_.substring(this.bookmark_, end);
            this.skipWhitespace_();
            return result;
        },
        /**
         * Moves the bookmark to the starting index of the next token
         * 
         * @private
         */
        advanceBookmark_ : function() {
            while (this.bookmark_ > 0) {
                this.bookmark_ -= 1;
                var ch = null;
                if (this.bookmark_ > 0) {
                    ch = this.text_.charAt(this.bookmark_ - 1);
                    if (ch === " " || ch === '"' || ch === "'") {
                        break;
                    }
                    if (ch === "," || ch === "." || ch === "?" || ch === "!") {
                        break;
                    }
                }
                ch = this.text_.charAt(this.bookmark_);
                if (ch === "," || ch === "." || ch === "?" || ch === "!") {
                    break;
                }
                if (ch === '"' || ch === "'") {
                    break;
                }
            }
        },
        /**
         * Advances the bookmark by skipping continuous whitespace characters
         * 
         * @private
         */
        skipWhitespace_ : function() {
            while (true) {
                var ch = (this.bookmark_ > 0)
                    ? this.text_.charAt(this.bookmark_ - 1)
                    : "";
                if (ch === " ") {
                    this.bookmark_ -= 1;
                } else {
                    break;
                }
            }
        }
    };

    var tests = [ "This is a modern rock song", "This            long space",
            "I think, therefore I am.", "      ", "", "O", "Oi", "Oi!!", "Space ending     ",
            "My name is 'Che'!", " Right in the.middle haha!" ];

    tests.forEach(function(text) {
        console.log(text);
        console.log("Reversed:");
        var reader = new ReverseReader(text);
        while (reader.hasNext()) {
            console.log(reader.next());
        }
        console.log("--- End of test ---");
    });
})();