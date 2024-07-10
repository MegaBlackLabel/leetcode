#
# @lc app=leetcode id=2529 lang=python3
#
# [2529] Maximum Count of Positive Integer and Negative Integer
#

# @lc code=start
from typing import List


class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        return max(sum(num > 0 for num in nums), sum(num < 0 for num in nums))
# @lc code=end

