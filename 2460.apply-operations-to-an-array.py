#
# @lc app=leetcode id=2460 lang=python3
#
# [2460] Apply Operations to an Array
#

# @lc code=start
from typing import List


class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        ans = [0] * len(nums)

        for i in range(len(nums) - 1):
            if nums[i] == nums[i + 1]:
                nums[i] *= 2
                nums[i + 1] = 0

        i = 0
        for num in nums:
            if num > 0:
                ans[i] = num
                i += 1

        return ans
# @lc code=end

