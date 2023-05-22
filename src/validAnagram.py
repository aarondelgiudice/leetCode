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

def merge_sort(s):
    if len(s) <= 1:
        return s
    
    pivot = len(s) // 2
    left = merge_sort(s[:pivot])
    right = merge_sort(s[pivot:])

    result = []

    l_index = r_index = 0
    while l_index < len(left) and r_index < len(right):
        if left[l_index] < right[r_index]:
            result.append(left[l_index])
            l_index += 1
        else: # left[l_index] >= right[r_index]
            result.append(right[r_index])
            r_index += 1

    result += left[l_index:]
    result += right[r_index:]

    return result


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # sort
        # NOTE: sorting (especially merge sort) sucks as a solution
        # space and time complexity is terrible
        # also NOTE: can use `sort(s) == sort(t)` but that's kinda cheating
        return merge_sort(s) == merge_sort(t)

        # hashmap
        if len(s) != len(t):
            return False

        counter = {}
        for i in range(len(s)):
            # A: this effectively does the same thing as code block B
            counter[s[i]] = 1 + counter.get(s[i], 0)
            counter[t[i]] = counter.get(t[i], 0) - 1

            
            # B: this effectively does the same thing as code block A
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
