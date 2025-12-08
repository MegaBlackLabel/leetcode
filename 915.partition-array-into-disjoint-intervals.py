#
# @lc app=leetcode id=915 lang=python3
#
# [915] Partition Array into Disjoint Intervals
#

# @lc code=start
from typing import List


class Solution:
    def partitionDisjoint(self, nums: List[int]) -> int:
        
        n = len(nums)
        left_max = [0] * n
        right_min = [0] * n

        left_max[0] = nums[0]
        for i in range(1, n):
            left_max[i] = max(left_max[i - 1], nums[i])

        right_min[-1] = nums[-1]
        for i in range(n - 2, -1, -1):
            right_min[i] = min(right_min[i + 1], nums[i])

        for i in range(n - 1):
            if left_max[i] <= right_min[i + 1]:
                return i + 1

        return n
# @lc code=end

