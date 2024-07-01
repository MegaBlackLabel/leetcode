#
# @lc app=leetcode id=2485 lang=python3
#
# [2485] Find the Pivot Integer
#

# @lc code=start
import math


class Solution:
    def pivotInteger(self, n: int) -> int:
        y = (n * n + n) // 2
        x = int(math.sqrt(y))
    
        return x if x * x == y else -1
# @lc code=end

