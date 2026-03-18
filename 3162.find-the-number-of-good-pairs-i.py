#
# @lc app=leetcode id=3162 lang=python3
#
# [3162] Find the Number of Good Pairs I
#

# @lc code=start
from typing import List


class Solution:
    def numberOfPairs(self, nums1: List[int], nums2: List[int], k: int) -> int:
        return sum(num1 % (num2 * k) == 0 for num1 in nums1 for num2 in nums2)
# @lc code=end

