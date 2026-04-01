#
# @lc app=leetcode id=3232 lang=python3
#
# [3232] Find if Digit Game Can Be Won
#

# @lc code=start
from typing import List


class Solution:
    def canAliceWin(self, nums: List[int]) -> bool:
        single_digit_sum = 0
        double_digit_sum = 0

        for num in nums:
            if num < 10:
                single_digit_sum += num
            else:
                double_digit_sum += num
        
        return single_digit_sum != double_digit_sum
# @lc code=end

