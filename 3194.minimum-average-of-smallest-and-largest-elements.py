#
# @lc app=leetcode id=3194 lang=python3
#
# [3194] Minimum Average of Smallest and Largest Elements
#

# @lc code=start
from typing import List


class Solution:
    def minimumAverage(self, nums: List[int]) -> float:
        nums.sort()
        n = len(nums)
        
        return min((nums[i] + nums[n - 1 - i]) / 2 for i in range(n // 2))
# @lc code=end

