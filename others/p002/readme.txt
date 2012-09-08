A non-negative integer N is given. The maximal binary ones stretch of N is the length of the longest sequence of consecutive bits set to 1 in the binary representation of N. For example, consider N = 114067. Its binary representation is 11011110110010011. Its maximal binary ones stretch is equal to 4.

Write a function

    int max_binary_ones_stretch(int N); 

that, given a non-negative integer N, returns the maximal binary ones stretch of N.

Assume that:

        N is an integer within the range [0..2,147,483,647].

For example, given N = 114067, the function should return 4, as explained above.

Complexity:

        expected worst-case time complexity is O(log(N));
        expected worst-case space complexity is O(1).