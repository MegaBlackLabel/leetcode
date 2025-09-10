#
# @lc app=leetcode id=775 lang=python3
#
# [775] Global and Local Inversions
#

# @lc code=start
from typing import List


class Solution:
    def isIdealPermutation(self, nums: List[int]) -> bool:
        
        for i, num in enumerate(nums):
            if abs(num - i) > 1:
                return False

        return True
# @lc code=end

