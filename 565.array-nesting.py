#
# @lc app=leetcode id=565 lang=python3
#
# [565] Array Nesting
#

# @lc code=start
from typing import List


class Solution:
    def arrayNesting(self, nums: List[int]) -> int:
        
        """
        Find the length of the longest set S(k) = {nums[k], nums[nums[k]], nums[nums[nums[k]]], ...}
        where S(k) is the set of indices that can be reached starting from index k.
        """
        visited = [False] * len(nums)
        max_length = 0

        for i in range(len(nums)):
            if not visited[i]:
                current_length = 0
                current_index = i

                while not visited[current_index]:
                    visited[current_index] = True
                    current_index = nums[current_index]
                    current_length += 1

                max_length = max(max_length, current_length)

        return max_length
# @lc code=end

