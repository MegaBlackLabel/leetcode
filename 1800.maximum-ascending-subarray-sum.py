#
# @lc app=leetcode id=1800 lang=python3
#
# [1800] Maximum Ascending Subarray Sum
#

# @lc code=start
from typing import List


class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        max_sum = temp_sum = nums[0] 
      
        for i in range(1, len(nums)):
            if nums[i] > nums[i - 1]:
                temp_sum += nums[i]
            else:
                temp_sum = nums[i]

            max_sum = max(max_sum, temp_sum)
      
        return max_sum 

# @lc code=end

