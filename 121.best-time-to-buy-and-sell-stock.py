#
# @lc app=leetcode id=121 lang=python3
#
# [121] Best Time to Buy and Sell Stock
#

# @lc code=start
from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        mx, mn = 0, float("inf")
        for price in prices:
            mn = min(mn, price)
            pro = price - mn
            mx = max(mx, pro)
        return mx


# @lc code=end
