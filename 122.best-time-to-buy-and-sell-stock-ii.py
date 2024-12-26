#
# @lc app=leetcode id=122 lang=python3
#
# [122] Best Time to Buy and Sell Stock II
#

# @lc code=start
import math
from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        sell = 0
        hold = -math.inf

        for price in prices:
            sell = max(sell, hold + price)
            hold = max(hold, sell - price)

        return sell
# @lc code=end

