"""
Given two strings s and t, return true if t is an anagram of s, and false otherwise.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

 

Example 1:

Input: s = "anagram", t = "nagaram"
Output: true
Example 2:

Input: s = "rat", t = "car"
Output: false
 

Constraints:

1 <= s.length, t.length <= 5 * 104
s and t consist of lowercase English letters.
 

Follow up: What if the inputs contain Unicode characters? How would you adapt your solution to such a case?

source: https://leetcode.com/problems/valid-anagram/
"""

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        counter = {}
        for i in range(len(s)):
            counter[s[i]] = 1 + counter.get(s[i], 0)
            counter[t[i]] = counter.get(t[i], 0) - 1

            # if s[i] in counter.keys():
            #     counter[s[i]] += 1

            # else:
            #     counter[s[i]] = 1

            # if t[i] in counter.keys():
            #     counter[t[i]] -= 1

            # else:
            #     counter[t[i]] = -1
 
        return any(counter.values()) == 0


# -----------------------------------------------------------------------------
# run solution
# -----------------------------------------------------------------------------
if __name__ == "__main__":
    INPUTS = (
        # s: str, t: str            output: bool
        (("anagram", "nagaram"),    True),
        (("rat", "car"),            False),
    )

    mySolution = Solution()

    for inputs, expected in INPUTS:
        print(f"s, t: {inputs}, isAnagram: {expected}")
        actual = mySolution.isAnagram(*inputs)
        print(f"actual: {actual}, expected: {expected}")
        if expected != actual:
            raise RuntimeError(f"acutal value does not match expected: actual={actual}, expected={expected}")
