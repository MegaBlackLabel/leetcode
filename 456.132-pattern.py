#
# @lc app=leetcode id=456 lang=python3
#
# [456] 132 Pattern
#

# @lc code=start
from typing import List


class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        
        stack = []
        second = float('-inf')

        for num in reversed(nums):
            if num < second:
                return True
            while stack and num > stack[-1]:
                second = stack.pop()
            stack.append(num)

        return False
# @lc code=end

