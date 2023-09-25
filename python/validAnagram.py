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
from typing import List


def merge_sort(s) -> List:
    """
    merge sort implementation
        Time: O(n log n)
        Space: O(n)
    
    Args:
        s: List or str

    Returns:
        List

    Raises:
        n/a
    """
    # base case
    # return s if s is null or is too short
    if not s or len(s) <= 1:
        return s
    
    # find pivot point -> halfway point in s
    pivot = len(s) // 2

    # recursively sort left and right halves
    left, right = s[:pivot], s[pivot:]
    left, right = merge_sort(left), merge_sort(right)

    # merge left and right halves in sorted orfer
    s_sorted = []
    l_index = r_index = 0

    while l_index < len(left) and r_index < len(right):
        if left[l_index] < right[r_index]:
            s_sorted.append(left[l_index])
            l_index += 1
        else: # left[l_index] >= right[r_index]
            s_sorted.append(right[r_index])
            r_index += 1

    # append to s_sorted any remaining values in left, right
    s_sorted += left[l_index:]
    s_sorted += right[r_index:]

    return s_sorted


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # one liner... kinda
        # sorting sucks as a solution as far as time and memory complexity
        # NOTE: you can use sorted(s) == sorted(t) but that's no fun 
        # return merge_sort(s) == merge_sort(t)
        
        # better solution: hashmap
        # edge cases
        if not s and not t: # s and t are null
            return True
        if not s or not t: # only one of s and t is null
            return False
        if len(s) != len(t): # anagrams must be of equal size
            return False
        
        sCounts, tCounts = {}, {}
        
        for i in range(len(s)):
            sCounts[s[i]] = 1 + sCounts.get(s[i], 0)
            tCounts[t[i]] = 1 + tCounts.get(t[i], 0)

        return sCounts == tCounts

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
