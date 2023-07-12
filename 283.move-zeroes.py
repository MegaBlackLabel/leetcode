#
# @lc app=leetcode id=283 lang=python3
#
# [283] Move Zeroes
#


# @lc code=start
from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        h = -1
        for i in range(len(nums)):
            if nums[i] != 0:
                h += 1
                nums[h], nums[i] = nums[i], nums[h]


# @lc code=end
