#
# @lc app=leetcode id=724 lang=python3
#
# [724] Find Pivot Index
#

# @lc code=start
from typing import List


class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        summ = sum(nums)
        prefix = 0

        for i, num in enumerate(nums):
            if prefix == summ - prefix - num:
                return i
            prefix += num

        return -1
# @lc code=end

