#
# @lc app=leetcode id=1608 lang=python3
#
# [1608] Special Array With X Elements Greater Than or Equal X
#

# @lc code=start
import itertools
from typing import List


class Solution:
    def specialArray(self, nums: List[int]) -> int:
        nums.sort()

        if nums[0] >= len(nums):
            return len(nums)

        for i, (a, b) in enumerate(itertools.pairwise(nums)):
            count = len(nums) - i - 1
            if a < count and b >= count:
                return count

        return -1
# @lc code=end

