#
# @lc app=leetcode id=136 lang=python3
#
# [136] Single Number
#

# @lc code=start
from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        dict = {}

        for n in nums:
            if n in dict:
                dict[n] += 1
            else:
                dict[n] = 1

        for key, val in dict.items():
            if val == 1:
                return key


# @lc code=end
