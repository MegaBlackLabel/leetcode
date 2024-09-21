#
# @lc app=leetcode id=2932 lang=python3
#
# [2932] Maximum Strong Pair XOR I
#

# @lc code=start
from typing import List


class Solution:
    def maximumStrongPairXor(self, nums: List[int]) -> int:
        return max(x ^ y for x in nums for y in nums if abs(x - y) <= min(x, y))
# @lc code=end

