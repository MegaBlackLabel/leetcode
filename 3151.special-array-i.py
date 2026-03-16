#
# @lc app=leetcode id=3151 lang=python3
#
# [3151] Special Array I
#

# @lc code=start
from itertools import pairwise
from typing import List


class Solution:
    def isArraySpecial(self, nums: List[int]) -> bool:
        
        return all(a % 2 != b % 2 for a, b in pairwise(nums))
# @lc code=end

