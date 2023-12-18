#
# @lc app=leetcode id=1480 lang=python3
#
# [1480] Running Sum of 1d Array
#

# @lc code=start
import itertools
from typing import List


class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        return itertools.accumulate(nums)
    
# @lc code=end

