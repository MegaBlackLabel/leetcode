#
# @lc app=leetcode id=1991 lang=python3
#
# [1991] Find the Middle Index in Array
#

# @lc code=start
from typing import List


class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        prefix = 0
        suffix = sum(nums)

        for i, num in enumerate(nums):
            suffix -= num
            if prefix == suffix:
                return i
            
            prefix += num

        return -1
# @lc code=end

