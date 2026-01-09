#
# @lc app=leetcode id=962 lang=python3
#
# [962] Maximum Width Ramp
#

# @lc code=start
from typing import List


class Solution:
    def maxWidthRamp(self, nums: List[int]) -> int:
        
        n = len(nums)
        stack = []

        for i in range(n):
            if not stack or nums[i] < nums[stack[-1]]:
                stack.append(i)

        max_width = 0

        for j in range(n - 1, -1, -1):
            while stack and nums[j] >= nums[stack[-1]]:
                i = stack.pop()
                max_width = max(max_width, j - i)

        return max_width
# @lc code=end

