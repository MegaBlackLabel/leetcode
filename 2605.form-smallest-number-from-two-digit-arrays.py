#
# @lc app=leetcode id=2605 lang=python3
#
# [2605] Form Smallest Number From Two Digit Arrays
#

# @lc code=start
from typing import List


class Solution:
    def minNumber(self, nums1: List[int], nums2: List[int]) -> int:
        return min(a if a == b else min(a, b) * 10 + max(a, b)
               for a in nums1
               for b in nums2)
# @lc code=end

