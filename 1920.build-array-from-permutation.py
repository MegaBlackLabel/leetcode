#
# @lc app=leetcode id=1920 lang=python3
#
# [1920] Build Array from Permutation
#

# @lc code=start
from typing import List


class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        n = len(nums)

        for i, num in enumerate(nums):
            nums[i] += n * (nums[num] % n)

        for i in range(n):
            nums[i] //= n

        return nums
# @lc code=end

