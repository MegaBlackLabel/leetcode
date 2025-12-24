#
# @lc app=leetcode id=945 lang=python3
#
# [945] Minimum Increment to Make Array Unique
#

# @lc code=start
from typing import List


class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:
        
        nums.sort()
        moves = 0
        for i in range(1, len(nums)):
            if nums[i] <= nums[i - 1]:
                needed = nums[i - 1] + 1 - nums[i]
                moves += needed
                nums[i] += needed
        return moves
# @lc code=end

