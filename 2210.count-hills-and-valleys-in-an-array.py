#
# @lc app=leetcode id=2210 lang=python3
#
# [2210] Count Hills and Valleys in an Array
#

# @lc code=start
from typing import List


class Solution:
    def countHillValley(self, nums: List[int]) -> int:
        ans = 0
        left = nums[0]

        for i in range(1, len(nums) - 1):
            if left < nums[i] and nums[i] > nums[i + 1] or left > nums[i] and nums[i] < nums[i + 1]:
                ans += 1
                left = nums[i]

        return ans
# @lc code=end

