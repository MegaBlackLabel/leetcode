#
# @lc app=leetcode id=2395 lang=python3
#
# [2395] Find Subarrays With Equal Sum
#

# @lc code=start
from typing import List


class Solution:
    def findSubarrays(self, nums: List[int]) -> bool:
        seen = set()

        for a, b in zip(nums, nums[1:]):
            summ = a + b
            if summ in seen:
                return True
            seen.add(summ)

        return False
# @lc code=end

