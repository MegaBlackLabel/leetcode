#
# @lc app=leetcode id=2824 lang=python3
#
# [2824] Count Pairs Whose Sum is Less than Target
#

# @lc code=start
from typing import List


class Solution:
    def countPairs(self, nums: List[int], target: int) -> int:
        return sum(nums[i] + nums[j] < target
               for i in range(len(nums))
               for j in range(i + 1, len(nums)))
# @lc code=end

