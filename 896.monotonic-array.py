#
# @lc app=leetcode id=896 lang=python3
#
# [896] Monotonic Array
#

# @lc code=start
from typing import List


class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        increasing = True
        decreasing = True

        for i in range(1, len(nums)):
            increasing &= nums[i - 1] <= nums[i]
            decreasing &= nums[i - 1] >= nums[i]

        return increasing or decreasing
# @lc code=end

