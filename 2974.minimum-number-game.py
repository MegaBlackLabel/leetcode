#
# @lc app=leetcode id=2974 lang=python3
#
# [2974] Minimum Number Game
#

# @lc code=start
from typing import List


class Solution:
    def numberGame(self, nums: List[int]) -> List[int]:
        nums.sort()
        
        return [nums[i + 1] if i % 2 == 0 else nums[i - 1] for i in range(len(nums))]
# @lc code=end

