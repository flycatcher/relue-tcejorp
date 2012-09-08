Write a function

    class Solution { public int hex_bitcount(String S); } 

that, given a string S consisting of N characters containing a big-endian hexadecimal representation of a non-negative integer M, returns the number of bits set to 1 in the binary representation of number M.

Assume that:

        N is an integer within the range [1..100,000];
        string S consists only of the following characters: 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, A, B, C, D, E and/or F.

For example, given S = "2F", the function should return 5, because string "2F" represents number 47, the binary representation of number 47 is 101111 and it contains five bits set to 1.

Complexity:

        expected worst-case time complexity is O(N);
        expected worst-case space complexity is O(1) (not counting the storage required for input arguments).