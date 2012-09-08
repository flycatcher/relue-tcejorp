An integer P is a whole cube if it is a cube of another integer Q; i.e. if P = Q^3.

Write a function:

class Solution { int whole_cubes_count(int A,int B); }

that returns the number of whole cubes that belong to the interval [A; B] (both ends included).

For example, given A = 8 and B = 65 the function should return 3, because there are three whole cubes within the interval [8..65], namely 8 = 2^3, 27 = 3^3 and 64 = 4^3.

Assume that:

A is an integer within the range [−2,147,483,648..2,147,483,647]; B is an integer within the range [−2,147,483,648..2,147,483,647]; A ≤ B. Complexity:

expected worst-case time complexity is O(CubeRoot(B)); expected worst-case space complexity is O(1). Notation used:

CubeRoot − a function which, for a given number X, returns a number Y such that Y^3 = X.