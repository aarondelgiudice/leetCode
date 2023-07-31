"""
712. Minimum ASCII Delete Sum for Two Strings

Given two strings s1 and s2, return the lowest ASCII sum of deleted characters to make two strings equal.

Example 1:
Input: s1 = "sea", s2 = "eat"
Output: 231
Explanation: Deleting "s" from "sea" adds the ASCII value of "s" (115) to the sum.
Deleting "t" from "eat" adds 116 to the sum.
At the end, both strings are equal, and 115 + 116 = 231 is the minimum sum possible to achieve this.

Example 2:
Input: s1 = "delete", s2 = "leet"
Output: 403
Explanation: Deleting "dee" from "delete" to turn the string into "let",
adds 100[d] + 101[e] + 101[e] to the sum.
Deleting "e" from "leet" adds 101[e] to the sum.
At the end, both strings are equal to "let", and the answer is 100+101+101+101 = 403.
If instead we turned both strings into "lee" or "eet", we would get answers of 433 or 417, which are higher.

Constraints:
1 <= s1.length, s2.length <= 1000
s1 and s2 consist of lowercase English letters.
"""


class Solution:
    def minimumDeleteSum(self, s1: str, s2: str) -> int:
        # swap s1, s2 if the length of s1 is greater than the length of s2
        # this will ensure that we use less space in our solution
        if len(s1) > len(s2):
            s1, s2 = s2, s1

        # initialize an array of zeros equal to len(s2) + 1
        prev_row = [0] * (len(s2) + 1)

        # fill prev_row with the rolling sum of ASCII values
        # e.g. for s2 == "eat"
        # prev_row[0] = 0
        # prev_row[1] = prev_row[0] + ord("eat"[0]) -> 0 + 101 -> 101
        # prev_row[2] = prev_row[1] + ord("eat"[1]) -> 101 + 97 -> 198
        # prev_row[3] = prev_row[2] + ord("eat"[-1]) -> 198 + 116 -> 314
        for j in range(1, len(s2)+1): 
            prev_row[j] = prev_row[j-1] + ord(s2[j-1]) 

        # loop over s1; for each character in s1 create a new array, curr_row
        # curr_row 
        for i in range(1, len(s1)+1): 
            curr_row = [prev_row[0] + ord(s1[i-1])] 
            
            for j in range(1, len(s2)+1): 
                if s1[i-1] == s2[j-1]: 
                    curr_row.append(prev_row[j-1]) 
            
                else: # s1[i - 1] != s2[j - 1]
                    curr_row.append(min(prev_row[j] + ord(s1[i-1]), curr_row[j-1] + ord(s2[j-1]))) 
            
            prev_row = curr_row 

        return prev_row[-1] 


if __name__ == "__main__":
    INPUTS = (
        # s1        s2      expected
        ("sea",     "eat",  231),
        ("delete",  "leet", 403),
    )

    for s1, s2, expected in INPUTS:
        actual = Solution().minimumDeleteSum(s1, s2)
        assert actual == expected, f"{actual=}, {expected=}"
