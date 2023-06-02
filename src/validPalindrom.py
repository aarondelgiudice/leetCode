"""
A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

Given a string s, return true if it is a palindrome, or false otherwise.

Example 1:
Input: s = "A man, a plan, a canal: Panama"
Output: true
Explanation: "amanaplanacanalpanama" is a palindrome.

Example 2:
Input: s = "race a car"
Output: false
Explanation: "raceacar" is not a palindrome.

Example 3:
Input: s = " "
Output: true
Explanation: s is an empty string "" after removing non-alphanumeric characters.
Since an empty string reads the same forward and backward, it is a palindrome.
 

Constraints:
1 <= s.length <= 2 * 105
s consists only of printable ASCII characters.

source: https://leetcode.com/problems/valid-palindrome/description/
"""

class Solution:
    def isPalindrome(self, s: str) -> bool:
        if not s:
            return True

        left, right = 0, len(s)-1

        while left < right:
            while left < right and not s[left].isalnum():
                left += 1

            while right > left and not s[right].isalnum():
                right -= 1

            if s[left].lower() != s[right].lower():
                return False

            else:
                left += 1
                right -= 1

        return True
    
if __name__ == "__main__":
    INPUTS = (
        # input: str                        output: bool
        ("A man, a plan, a canal: Panama",  True),
        ("race a car",                      False),
        (" ",                               True),
    )
     
    for input, expected in INPUTS:
        actual = Solution().isPalindrome(input)
        print(input, actual, expected)
        assert actual == expected, f"{input=}, {expected=}, {actual=}"
