#
# @lc app=leetcode id=3131 lang=python3
#
# [3131] Find the Integer Added to Array I
#

# @lc code=start
from typing import List


class Solution:
    def addedInteger(self, nums1: List[int], nums2: List[int]) -> int:
        
        min_nums2 = min(nums2)
        min_nums1 = min(nums1)
        return min_nums2 - min_nums1
# @lc code=end

