#
# @lc app=leetcode id=2869 lang=python3
#
# [2869] Minimum Operations to Collect Elements
#

# @lc code=start
from typing import List


class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        seen = set()

        for i, num in enumerate(reversed(nums)):
            if num > k:
                continue
            seen.add(num)
            if len(seen) == k:
                return i + 1
# @lc code=end

