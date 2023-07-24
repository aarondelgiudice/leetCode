"""
50. Pow(x, n)

Implement pow(x, n), which calculates x raised to the power n (i.e., xn).

Example 1:
Input: x = 2.00000, n = 10
Output: 1024.00000

Example 2:
Input: x = 2.10000, n = 3
Output: 9.26100

Example 3:
Input: x = 2.00000, n = -2
Output: 0.25000
Explanation: 2**-2 = (1/2)**2 = 1/4 = 0.25

Constraints:
-100.0 < x < 100.0
-2**31 <= n <= (2**31)-1
n is an integer.
Either x is not zero or n > 0.
-10**4 <= x**n <= 10**4
"""

class Solution:
    def myPow(self, x: float, n: int) -> float:
        # one-liner
        # return x**n

        def helper(x, n):
            # base case(s)
            # 0**n = 0
            if x == 0: return 0

            # x**0 = 1
            if n == 0: return 1

            # first, solve sub problem:
            # res = x**n//2
            res = helper(x, n // 2)

            # next, solve current problem:
            # res = (x**n//2) * (x**n//2) -> res * res
            res = res * res
            
            # lastly, handle even-odd cases:
            # if n is even, then n//2 == n/2
            # e.g. x^4 == x^2 * x^2
            if n % 2 == 0:
                return res

            # if n is odd, then n//2 != n/2
            # therefore, we need to multiply by x one more time
            # e.g. x^5 == x^2 * x^2 * x
            else: # n % 2 != 0
                return x * res
        
        # perform recursion
        res = helper(x, abs(n))

        # if positive n:
        # Pow(x, n) -> x*x*x*...*x (n times)
        if n >= 0:
            return res

        # else negative n:
        # Pow(x, n) -> 1/(x*x*x*...*x) (n times)
        else:
            return 1/res


if __name__ == "__main__":
    INPUTS = (
        # x         n   expected
        (2.00000,   10, 1024.00000),
        (2.10000,   3,  9.26100),
        (2.00000,   -2, 0.25000),
    )

    for x, n, expected in INPUTS:
        actual = Solution().myPow(x, n)
        
        # sanity check for rounding errors
        actual = round(actual, 5)
        expected = round(expected, 5)

        assert actual == expected, f"{expected=}, {actual=}"
