#
# @lc app=leetcode id=3392 lang=python3
#
# [3392] Count Subarrays of Length Three With a Condition
#

# @lc code=start
from typing import List


class Solution:
    def countSubarrays(self, nums: List[int]) -> int:
        return sum(1 for i in range(1, len(nums) - 1) 
                   if (nums[i-1] + nums[i+1]) * 2 == nums[i])



# @lc code=end

