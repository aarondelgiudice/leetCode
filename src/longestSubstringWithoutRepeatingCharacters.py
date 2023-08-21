"""
3. Longest Substring Without Repeating Characters
Given a string s, find the length of the longest substring without repeating characters.

Example 1:
Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.

Example 2:
Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.

Example 3:
Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.

Constraints:
0 <= s.length <= 5 * 10**4
s consists of English letters, digits, symbols and spaces.
"""

INPUTS = (
    # s             expected
    ("abcabcbb",    3),
    ("bbbbb",       1),
    ("pwwkew",      3),
)

def main():
    for s, expected in INPUTS:
        result = Solution().lengthOfLongestSubstring(s)
        assert result == expected, f"{s=}, {expected=}, {result=}"
    
    return


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        slow, fast = 0, 1
        maxLen = 0

        # NOTE use `<= len(s)` vs. `< len(s)`
        # b/c we're using index ranges (s[index1:index2])
        while fast <= len(s):
            subString = s[slow:fast]

            # check if substring is unique
            if len(subString) == len(set(subString)):
                # if unique: update max length variable
                maxLen = max(maxLen, fast-slow)
                
            else:
                # if not unique: speed up scanning by incrementing left pointer
                # slow = fast # not sure why `slow += 1` works vs. `slow = fast`
                slow += 1
                
            # continue scanning right pointer
            fast += 1

        return maxLen


if __name__ == "__main__":
    main()
