#
# @lc app=leetcode id=2917 lang=python3
#
# [2917] Find the K-or of an Array
#

# @lc code=start
from typing import List


class Solution:
    def findKOr(self, nums: List[int], k: int) -> int:
        kMaxBit = 30
        return sum(2**i for i in range(kMaxBit + 1) if sum(num >> i & 1 for num in nums) >= k)
# @lc code=end

