#
# @lc app=leetcode id=2706 lang=python3
#
# [2706] Buy Two Chocolates
#

# @lc code=start
import math
from typing import List


class Solution:
    def buyChoco(self, prices: List[int], money: int) -> int:
        min1 = math.inf
        min2 = math.inf

        for price in prices:
            if price <= min1:
                min2 = min1
                min1 = price
            elif price < min2:
                min2 = price

        minCost = min1 + min2
        
        return money if minCost > money else money - minCost
# @lc code=end

