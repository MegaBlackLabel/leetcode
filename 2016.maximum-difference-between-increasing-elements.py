#
# @lc app=leetcode id=2016 lang=python3
#
# [2016] Maximum Difference Between Increasing Elements
#

# @lc code=start
from typing import List


class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        ans = -1
        mini = nums[0]

        for i in range(len(nums)):
            if nums[i] > mini:
                ans = max(ans, nums[i] - mini)
            mini = min(mini, nums[i])

        return ans
# @lc code=end

