#
# @lc app=leetcode id=287 lang=python3
#
# [287] Find the Duplicate Number
#

# @lc code=start
from typing import List


class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        low,high = nums[0],nums[nums[0]]
        while low != high:
            low,high = nums[low],nums[nums[high]]
        low = 0
        while low != high:
            low,high = nums[low],nums[high]
        return low
# @lc code=end

