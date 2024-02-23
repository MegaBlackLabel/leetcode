#
# @lc app=leetcode id=1827 lang=python3
#
# [1827] Minimum Operations to Make the Array Increasing
#

# @lc code=start
from typing import List


class Solution:
    def minOperations(self, nums: List[int]) -> int:
        ans = 0
        for idx, num in enumerate(nums):
            if idx > 0 and num <= nums[idx - 1]:
                to_incr = nums[idx - 1] - num + 1
                ans += to_incr
                nums[idx] += to_incr
        return ans
# @lc code=end

