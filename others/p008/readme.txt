Two non-negative integers A and B are given. Integer A occurs in integer B at position P if the decimal representation of A is a substring, starting at position P (counting from zero), of the decimal representation of B. Decimal representations are assumed to be big-endian and without leading zeros (the only exception being the number 0, whose decimal representation is "0").

For example, 53 occurs in 1953786 at position 2. 78 occurs in 195378678 at positions 4 and 7. 57 does not occur in 153786.

Write a function

int integer_decimal_occurrence(int A,int B);

that, given two non-negative integers A and B, returns the leftmost position at which A occurs in B. The function should return −1 if A does not occur in B.

For example, given A = 53 and B = 1953786, the function should return 2, as explained above.

Assume that:

A is an integer within the range [0..999,999,999];
B is an integer within the range [0..999,999,999].
Complexity:

expected worst-case time complexity is O(log(A)+log(B));
expected worst-case space complexity is O(log(A)+log(B)).