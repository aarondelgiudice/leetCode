"""
Given two strings s and t, return true if they are equal when both are typed into empty text editors. '#' means a
backspace character.

Note that after backspacing an empty text, the text will continue empty.

Example 1:
Input: s = "ab#c", t = "ad#c"
Output: true
Explanation: Both s and t become "ac".

Example 2:
Input: s = "ab##", t = "c#d#"
Output: true
Explanation: Both s and t become "".

Example 3:
Input: s = "a#c", t = "b"
Output: false
Explanation: s becomes "c" while t becomes "b".

Constraints:
1 <= s.length, t.length <= 200
s and t only contain lowercase letters and '#' characters.

Follow up: Can you solve it in O(n) time and O(1) space?

source: https://leetcode.com/problems/backspace-string-compare/
"""

class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        def traverse(self, x: str) -> str:
            stack = []
            while x:
                curr, x = x[0], x[1:]
                if curr == "#":
                    if stack:
                        stack.pop()
                else:
                    stack.append(curr)
            return "".join(stack)

if __name__ == "__main__":
    INPUTS = (
        # s         t       expected
        ("ab#c",    "ad#c", True),
        ("ab##",    "c#d#", True),
        ("a#c",     "b",    False),
    )

    for s, t, expected in INPUTS:
        actual = Solution().backspaceCompare(s, t)
        assert actual == expected, (actual, expected)
