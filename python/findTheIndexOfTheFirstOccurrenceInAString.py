"""
Given two strings needle and haystack, return the index of the first occurrence of needle in haystack, or -1 if needle
is not part of haystack.

Example 1:
Input: haystack = "sadbutsad", needle = "sad"
Output: 0
Explanation: "sad" occurs at index 0 and 6.
The first occurrence is at index 0, so we return 0.

Example 2:
Input: haystack = "leetcode", needle = "leeto"
Output: -1
Explanation: "leeto" did not occur in "leetcode", so we return -1.
 

Constraints:
1 <= haystack.length, needle.length <= 10**4
haystack and needle consist of only lowercase English characters.

source: https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/
"""

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if len(needle) == 0:
            return 0
        
        # Rabin-Karp, optimal solution
        # Rabin-Karp alog: https://www.geeksforgeeks.org/rabin-karp-algorithm-for-pattern-searching/
        hash_n = hash(needle)
        for i in range(len(haystack)-len(needle)+1):
            if hash(haystack[i:i+len(needle)]) == hash_n:
                return i
        return -1
    
        # two pointer AKA stride-lite
        left, right = 0, 1
        while right <= len(haystack):
            while right < len(needle):
                right += 1
            if haystack[left:right] == needle:
                return left
            else:
                left += 1
                right += 1
        return -1
        
        # better stride method
        steps = len(haystack)-len(needle)+1
        
        for i in range(steps):
            if haystack[i:i+len(needle)] == needle:
                return i
        
        return -1
    
        # hacky one-liner
        return haystack.find(needle)

if __name__ == "__main__":
    INPUTS = (
        # haystack, needle, expected
        ("sadbutsad", "sad", 0),
        ("leetcode", "leeto", -1),
    )

    for haystack, needle, expected in INPUTS:
        actual = Solution().strStr(haystack, needle)
        assert actual == expected, (actual, expected)
