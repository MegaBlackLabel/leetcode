#
# @lc app=leetcode id=3028 lang=python3
#
# [3028] Ant on the Boundary
#

# @lc code=start
from typing import List


class Solution:
    def returnToBoundaryCount(self, nums: List[int]) -> int:
        position = 0
        count = 0
        for move in nums:
            position += move
            if position == 0:
                count += 1
        return count
        

# @lc code=end

