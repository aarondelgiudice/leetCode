"""
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
 

Example 1:
Input: s = "()"
Output: true

Example 2:
Input: s = "()[]{}"
Output: true

Example 3:
Input: s = "(]"
Output: false
 

Constraints:

1 <= s.length <= 104
s consists of parentheses only '()[]{}'.

source: `https://leetcode.com/problems/valid-parentheses/`
"""

class Solution:
    def isValid(self, s: str) -> bool:
        opening = "{[("
        closing = "}])"
        brackets = {
            ')': '(',
            '}': '{',
            ']': '['
        }
        stack = []

        for char in s:
            if char in opening:
                stack.append(char)
            
            elif char in closing:
                if len(stack) == 0:
                    return False
                
                if stack[-1] == brackets[char]:
                    stack.pop(-1)
                
                else:
                    return False
        
        return len(stack) == 0


# -----------------------------------------------------------------------------
# run solution
# -----------------------------------------------------------------------------
if __name__ == "__main__":
    INPUTS = (
        # s: str,   output: bool
        ("()",      True),
        ("()[]{}",  True),
        ("(]",      False)
    )

    mySolution = Solution()

    for s, expected in INPUTS:
        print(f"input: {s}")
        actual = mySolution.isValid(s)
        print(f"expected: {expected}, actual: {actual}")
        if expected != actual:
            raise RuntimeError(f"acutal value does not match expected: actual={actual}, expected={expected}")
