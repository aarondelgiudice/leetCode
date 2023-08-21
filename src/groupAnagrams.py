"""
49. Group Anagrams

Given an array of strings strs, group the anagrams together. You can return the answer in any order.
An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

Example 1:
Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

Example 2:
Input: strs = [""]
Output: [[""]]

Example 3:
Input: strs = ["a"]
Output: [["a"]]

Constraints:
1 <= strs.length <= 10**4
0 <= strs[i].length <= 100
strs[i] consists of lowercase English letters.
"""

from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # hashmap solution
        anagram_map = {}

        for word in strs:
            # anagram -> sorted strings will be equal if both words are anagrams
            word_sorted = "".join(sorted(word))
            
            # sorted word is key in anagram_map
            # if sorted word is present, append new word to list
            if word_sorted in anagram_map.keys():
                anagram_map[word_sorted].append(word)

            # if sorted word is not present,
            # create a new list of potential anagrams with sorted word as the key
            else:
                anagram_map[word_sorted] = [word]
        
        # anagram_map.values() will contain a list of all anagrams
        return list(anagram_map.values())

if __name__ == "__main__":
    INPUTS = (
        # strs                                  expected
        (["eat","tea","tan","ate","nat","bat"], [["bat"],["nat","tan"],["ate","eat","tea"]]),
        ([""],                                  [[""]]),
        (["a"],                                 [["a"]])
    )

    for strs, expected in INPUTS:
        actual = Solution().groupAnagrams(strs)
        # TODO: sort actual
        # TODO: sort expected
        # TODO: assert sorted actual == sorted expected, f"{acutal=}, {expected=}"
    