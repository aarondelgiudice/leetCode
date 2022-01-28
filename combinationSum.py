"""
Given an array of distinct integers candidates and a target integer target, return a list of all unique combinations of candidates where the chosen numbers sum to target. You may return the combinations in any order.

The same number may be chosen from candidates an unlimited number of times. Two combinations are unique if the frequency of at least one of the chosen numbers is different.

It is guaranteed that the number of unique combinations that sum up to target is less than 150 combinations for the given input.

 

Example 1:

Input: candidates = [2,3,6,7], target = 7
Output: [[2,2,3],[7]]
Explanation:
2 and 3 are candidates, and 2 + 2 + 3 = 7. Note that 2 can be used multiple times.
7 is a candidate, and 7 = 7.
These are the only two combinations.
Example 2:

Input: candidates = [2,3,5], target = 8
Output: [[2,2,2,2],[2,3,3],[3,5]]
Example 3:

Input: candidates = [2], target = 1
Output: []
 

Constraints:

1 <= candidates.length <= 30
1 <= candidates[i] <= 200
All elements of candidates are distinct.
1 <= target <= 500

source: https://leetcode.com/problems/combination-sum/
"""

from typing import List

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        unique = {}
        candidates = list(set(candidates))
        self.solve(candidates, target, result, unique)
        return result
    
    def solve(self, candidates, target, result, unique, i=0, current=[]):
        if target == 0:
            temp = [i for i in current]
            temp1 = temp
            temp.sort()
            temp = tuple(temp)
            if temp not in unique:
                unique[temp] = 1
                result.append(temp1)
            return
        
        if target <0:
            return
        
        for x in range(i, len(candidates)):
            current.append(candidates[x])
            
            self.solve(candidates, target-candidates[x], result, unique, i, current)
            
            current.pop(len(current) - 1)
 

# -----------------------------------------------------------------------------
# run solution
# -----------------------------------------------------------------------------
if __name__ == "__main__":
    INPUTS = (
        # candidates: List[int],    tartget: int,   expected: List[int]
        ([2,3,6,7],                 7,              [[2,2,3],[7]]),
        ([2,3,5],                   8,              [[2,2,2,2],[2,3,3],[3,5]]),
        ([2],                       1,              [])
    )

    mySolution = Solution()

    for candidates, target, expected in INPUTS:
        print(f"candidates: {candidates}, target: {target}")
        actual = mySolution.combinationSum(candidates, target)
        print(f"expected: {expected}, actual: {actual}")
        if expected != actual:
            raise RuntimeError(f"acutal value does not match expected: actual={actual}, expected={expected}")