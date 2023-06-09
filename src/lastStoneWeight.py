"""
You are given an array of integers stones where stones[i] is the weight of the ith stone.

We are playing a game with the stones. On each turn, we choose the heaviest two stones and smash them together. Suppose the heaviest two stones have weights x and y with x <= y. The result of this smash is:

If x == y, both stones are destroyed, and
If x != y, the stone of weight x is destroyed, and the stone of weight y has new weight y - x.
At the end of the game, there is at most one stone left.

Return the weight of the last remaining stone. If there are no stones left, return 0.

Example 1:
Input: stones = [2,7,4,1,8,1]
Output: 1
Explanation: 
We combine 7 and 8 to get 1 so the array converts to [2,4,1,1,1] then,
we combine 2 and 4 to get 2 so the array converts to [2,1,1,1] then,
we combine 2 and 1 to get 1 so the array converts to [1,1,1] then,
we combine 1 and 1 to get 0 so the array converts to [1] then that's the value of the last stone.

Example 2:
Input: stones = [1]
Output: 1

Constraints:
1 <= stones.length <= 30
1 <= stones[i] <= 1000

source: https://leetcode.com/problems/last-stone-weight/
"""

import heapq
from typing import List


class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        weight = 0
        # max heap solution
        # python does not support max heap, only min heap
        # to spoof a max heap, first convert all elements to negative
        # and then add the negative numbers to a min heap
        stones = [-1*i for i in stones]
        heapq.heapify(stones)

        while len(stones) > 1:
            # get the two largest stones
            # technically these are the two smallest stones,
            # as we converted all values to negative numbers
            # heappop() will always pop the smallest (in our case, largest) element in a heap
            y = heapq.heappop(stones)
            x = heapq.heappop(stones)

            # update stone weights
            if x == y:
                pass # do nothing; both stones are destroyed

            if x != y:
                # if one stone is bigger, the smaller stone is destroyed
                # and the bigger has a new weight of y-x
                y -= x

                # add y with new weight back to the heap
                heapq.heappush(stones, y)

        if stones:
            # convert negative -> positive
            weight = -1*stones[0]

        return weight


if __name__ == "__main__":
    INPUTS = (
        # stones        # expected
        ([2,7,4,1,8,1], 1),
        ([1],           1),
    )

    for stones, expected in INPUTS:
        output = Solution().lastStoneWeight(stones)
        assert output == expected, f"{stones=}, {expected=}, {output=}"
