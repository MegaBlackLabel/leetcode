#
# @lc app=leetcode id=3300 lang=python3
#
# [3300] Minimum Element After Replacement With Digit Sum
#

# @lc code=start
from typing import List


class Solution:
    def minElement(self, nums: List[int]) -> int:
        min_digit_sum = float('inf')

        for num in nums:
            digit_sum = 0
            for digit_char in str(num):
                digit_sum += int(digit_char)
          
            min_digit_sum = min(min_digit_sum, digit_sum)
      
        return min_digit_sum
# @lc code=end

