"""
9. Palindrome Number
Difficulty: Easy

Given an integer x, return true if x is palindrome integer.

An integer is a palindrome when it reads the same backward as forward.

For example, 121 is a palindrome while 123 is not.
 

Example 1:

Input: x = 121
Output: true
Explanation: 121 reads as 121 from left to right and from right to left.
Example 2:

Input: x = -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.
Example 3:

Input: x = 10
Output: false
Explanation: Reads 01 from right to left. Therefore it is not a palindrome.
 

Constraints:

-231 <= x <= 231 - 1
 

Follow up: Could you solve it without converting the integer to a string?
"""
class Solution:
    def isPalindrome(self, x: int) -> bool:
        # handle edge cases
        if x is None or x < 0:
            return False

        if 0 <= x < 10:
            return True

        # solve
        """
        # convert to string
        if str(x) == str(x)[::-1]:
            return True
        else:
            return False
        """
        # solve w/o converting to string
        temp = x
        rev = 0
        while x > 0:
            dig = x % 10
            rev = rev * 10 + dig
            x = x // 10

        if temp == rev:
            return True

        else:
            return False

if __name__ == "__main__":
    INPUTS = (
        # x: int,   output: bool
        (121,       True),
        (-121,      False),
        (10,        False)
    )

    mySolution = Solution()

    for x, expected in INPUTS:
        print(f"input: {x}, output: {expected}")
        actual = mySolution.isPalindrome(x)
        print(f"expected: {expected}, actual: {actual}")
        if expected != actual:
            raise RuntimeError(f"acutal value does not match expected: actual={actual}, expected={expected}")
