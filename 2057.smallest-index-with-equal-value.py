#
# @lc app=leetcode id=2057 lang=python3
#
# [2057] Smallest Index With Equal Value
#

# @lc code=start
from typing import List


class Solution:
    def smallestEqual(self, nums: List[int]) -> int:
        return next((i for i, num in enumerate(nums) if i % 10 == num), -1)
# @lc code=end

