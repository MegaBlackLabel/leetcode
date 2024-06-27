#
# @lc app=leetcode id=2465 lang=python3
#
# [2465] Number of Distinct Averages
#

# @lc code=start
from typing import List


class Solution:
    def distinctAverages(self, nums: List[int]) -> int:
        n = len(nums)
        sums = set()

        nums.sort()

        for i in range(n // 2):
            sums.add(nums[i] + nums[n - 1 - i])

        return len(sums)
# @lc code=end

