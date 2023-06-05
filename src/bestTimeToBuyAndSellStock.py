"""
You are given an array prices where prices[i] is the price of a given stock on the ith day.

You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

Example 1:
Input: prices = [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.

Example 2:
Input: prices = [7,6,4,3,1]
Output: 0
Explanation: In this case, no transactions are done and the max profit = 0.
 
Constraints:
1 <= prices.length <= 10^5
0 <= prices[i] <= 10^4

source: https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
"""
from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # two pointer solution
        # initiate pointers, max profit
        # prices[left] -> buy price
        # prices[right] -> sell price
        # sell - buy -> profit
        left = 0
        right = 1
        max_profit = 0

        while right < len(prices):
            # check profitability
            if prices[right] > prices[left]:
                curr = prices[right] - prices[left]
                
                # if current profit (p) beats max profit (max_p), update max_p
                max_profit = max(curr, max_profit)
            
            else: # prices[right] <= prices[left]:
                # if buy price is less than sell price,
                # update left point to match right pointer
                left = right

            # regardless of condition, continue scanning array
            right += 1

        return max_profit
    
        # kadane's algorithm (two pointer solution is faster)
        max_profit = 0
        max_current = 0

        for i in range(1, len(prices)):
            # check if current profit is > 0
            buy_price, sell_price = prices[i], prices[i-1] # current day, previous day
            curr_profit = buy_price - sell_price

            # get max rolling profit -> sum(previous profit, current profit)
            max_current = max(0, max_current + curr_profit)

            # get max of current profit vs. max profit
            max_profit = max(max_profit, max_current)

        return max_profit



if __name__ == "__main__":
    INPUTS = (
        # input: List[int]          output: int
        ([7, 1, 5, 3, 6, 4],        5),
        ([7, 6, 4, 3, 1],           0),
    )

    for input, expected in INPUTS:
        actual = Solution().maxProfit(input)
        assert actual == expected, f"{input=}, {expected=}, {actual=}"