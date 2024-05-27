#
# @lc app=leetcode id=2303 lang=python3
#
# [2303] Calculate Amount Paid in Taxes
#

# @lc code=start
from typing import List


class Solution:
    def calculateTax(self, brackets: List[List[int]], income: int) -> float:
        ans = 0
        prev = 0

        for upper, percent in brackets:
            if income < upper:
                return ans + (income - prev) * percent / 100.0
            ans += (upper - prev) * percent / 100.0
            prev = upper

        return ans
    
# @lc code=end

