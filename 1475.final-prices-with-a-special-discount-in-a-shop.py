#
# @lc app=leetcode id=1475 lang=python3
#
# [1475] Final Prices With a Special Discount in a Shop
#

# @lc code=start
from typing import List


class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        ans = prices.copy()
        stack = []

        for i, price in enumerate(prices):
            while stack and prices[stack[-1]] >= price:
                ans[stack.pop()] -= price
            stack.append(i)

        return ans
# @lc code=end

