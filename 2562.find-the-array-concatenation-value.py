#
# @lc app=leetcode id=2562 lang=python3
#
# [2562] Find the Array Concatenation Value
#

# @lc code=start
from typing import List


class Solution:
    def findTheArrayConcVal(self, nums: List[int]) -> int:
        ans = 0
        i, j = 0, len(nums) - 1
        while i < j:
            ans += int(str(nums[i]) + str(nums[j]))
            i, j = i + 1, j - 1
        if i == j:
            ans += nums[i]
        return ans
# @lc code=end

