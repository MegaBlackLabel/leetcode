#
# @lc app=leetcode id=3467 lang=python3
#
# [3467] Transform Array by Parity
#

# @lc code=start
from typing import List


class Solution:
    def transformArray(self, nums: List[int]) -> List[int]:
        even_count = sum(1 for num in nums if num % 2 == 0)
        return [0] * even_count + [1] * (len(nums) - even_count)
# @lc code=end

