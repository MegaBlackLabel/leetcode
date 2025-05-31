#
# @lc app=leetcode id=503 lang=python3
#
# [503] Next Greater Element II
#

# @lc code=start
from typing import List


class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        
        """
        This function finds the next greater element for each element in a circular array.
        It uses a stack to keep track of indices of elements for which we haven't found the next greater element yet.
        """
        n = len(nums)
        result = [-1] * n
        stack = []

        for i in range(n * 2):
            num = nums[i % n]
            while stack and nums[stack[-1]] < num:
                result[stack.pop()] = num
            if i < n:
                stack.append(i)

        return result       
# @lc code=end

