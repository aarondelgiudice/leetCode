"""
Given a string s, return the longest palindromic substring in s.

 

Example 1:

Input: s = "babad"
Output: "bab"
Explanation: "aba" is also a valid answer.
Example 2:

Input: s = "cbbd"
Output: "bb"
 

Constraints:

1 <= s.length <= 1000
s consist of only digits and English letters.

source: https://leetcode.com/problems/longest-palindromic-substring/
"""

class Solution:
    def longestPalindrome(self, s: str) -> str:        
        # handle edge cases
        if s == "":  # s is an empty string
            return s

        if s == len(s) * s[0]:  # s is a single character (e.g. s="a") or a single character repeated (e.g s="aaa")
            return s
        
        maxSubString = s[0]
        
        for start_pos in range(len(s) - 1)[::-1]:
            for end_pos in range(start_pos + 1, len(s)):
                if s[start_pos] == s[end_pos]:
                    subString = s[start_pos:end_pos + 1]
                    
                    if subString == subString[::-1]:  # palindrome
                        if len(subString) > len(maxSubString):
                            maxSubString = subString 
        
        return maxSubString


# -----------------------------------------------------------------------------
# run solution
# -----------------------------------------------------------------------------
if __name__ == "__main__":
    INPUTS = (
        # input: str,   output: str
        ("babad",       "'bab' or 'aba'",),
        ("cbbd",        "bb",),
    )

    mySolution = Solution()

    for s, expected in INPUTS:
        print(f"input: {s}")
        actual = mySolution.longestPalindrome(s)
        print(f"expected: {expected}, actual: {actual}")
