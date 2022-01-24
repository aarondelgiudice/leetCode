"""
Given an integer n, return the number of prime numbers that are strictly less than n.

Example 1:
Input: n = 10
Output: 4
Explanation: There are 4 prime numbers less than 10, they are 2, 3, 5, 7.

Example 2:
Input: n = 0
Output: 0

Example 3:
Input: n = 1
Output: 0

Constraints:
0 <= n <= 5 * 106

source: https://leetcode.com/problems/count-primes/
"""
from typing import List

def get_seive(n: int) -> List[bool]:
    factors = [0, 1]

    mask = [True] * n


    for i in range(n):
        if i in factors:
            mask[i] = False

        if mask[i]:
            for j in range(i * 2, n, i):
                mask[j] = False

    return mask


class Solution:
    def countPrimes(self, n: int) -> int:
        return sum(get_seive(n))


# -----------------------------------------------------------------------------
# run solution
# -----------------------------------------------------------------------------
if __name__ == "__main__":
    INPUTS = (
        # input: int,   output: int
        (10,            4),
        (0,             0),
        (1,             0)
    )

    mySolution = Solution()

    for num, expected in INPUTS:
        print(f"input: {num}")
        actual = mySolution.countPrimes(num)
        print(f"expected: {expected}, actual: {actual}")
        if expected != actual:
            raise RuntimeError(f"acutal value does not match expected: actual={actual}, expected={expected}")

