#
# @lc app=leetcode id=2996 lang=python3
#
# [2996] Smallest Missing Integer Greater Than Sequential Prefix Sum
#

# @lc code=start
from typing import List


class Solution:
    def missingInteger(self, nums: List[int]) -> int:
        numsSet = set(nums)
        ans = nums[0]

        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1] + 1:
                break
            ans += nums[i]

        while ans in numsSet:
            ans += 1

        return ans
# @lc code=end

