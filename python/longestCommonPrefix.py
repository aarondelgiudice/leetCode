"""
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

 

Example 1:

Input: strs = ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
 

Constraints:

1 <= strs.length <= 200
0 <= strs[i].length <= 200
strs[i] consists of only lowercase English letters.

source: `https://leetcode.com/problems/longest-common-prefix/`
"""
from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # # easy to understand solution
        # prefix = ""
    
        # # this can be replaced with min(strs), max(strs)
        # # but WTF sorts lists alphabetically with min(), max()?
        # # strs = sorted(strs)
        # # first_word, last_word = strs[0], strs[-1]
        # first_word, last_word = min(strs), max(strs)
        
        # # loop
        # i = 0
        # N = min(len(first_word), len(last_word))
            
        # while i < N:
        #     # if chars are equal
        #     if first_word[i] == last_word[i]:
        #         # add this char to the prefix
        #         prefix += first_word[i]

        #     else:
        #         # if no match, break loop
        #         break
            
        #     # increment index
        #     i += 1

        # better solution
        prefix = strs[0] # starting position is arbitrary

        for word in strs:
            while not word.startswith(prefix):
                # if word does not start with prefix,
                # drop last letter from prefix until a match is found
                # while loop will end if prefix == "", i.e. no match found
                prefix = prefix[:-1]

        # return longest common prefix or ""
        return prefix

if __name__ == "__main__":
    INPUTS = (
        # s: List[str],                 output: str
        (["flower","flow","flight"],    "fl"),
        (["dog","racecar","car"],       ""),
    )

    mySolution = Solution()

    for strs, expected in INPUTS:
        print(f"input: {strs}")
        actual = mySolution.longestCommonPrefix(strs)
        print(f"expected: {expected}, actual: {actual}")
        if expected != actual:
            raise RuntimeError(f"acutal value does not match expected: actual={actual}, expected={expected}")
