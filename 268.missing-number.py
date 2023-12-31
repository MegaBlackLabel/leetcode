#
# @lc app=leetcode id=268 lang=python3
#
# [268] Missing Number
#

# @lc code=start
from typing import List


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        len_n = len(nums)
        res = len_n

        for i in range(len_n):
            res += i - nums[i]

        return res


# @lc code=end
