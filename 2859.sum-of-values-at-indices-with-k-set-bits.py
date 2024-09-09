#
# @lc app=leetcode id=2859 lang=python3
#
# [2859] Sum of Values at Indices With K Set Bits
#

# @lc code=start
from typing import List


class Solution:
    def sumIndicesWithKSetBits(self, nums: List[int], k: int) -> int:
        return sum(num for i, num in enumerate(nums)
               if i.bit_count() == k)
# @lc code=end

