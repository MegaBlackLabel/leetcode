#
# @lc app=leetcode id=581 lang=python3
#
# [581] Shortest Unsorted Continuous Subarray
#

# @lc code=start
from typing import List


class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        
        """
        Find the shortest unsorted continuous subarray in a given list of integers.

        Args:
        nums (List[int]): The input list of integers.

        Returns:
        int: The length of the shortest unsorted continuous subarray.
        """
        if not nums:
            return 0

        sorted_nums = sorted(nums)
        start, end = 0, len(nums) - 1

        while start < len(nums) and nums[start] == sorted_nums[start]:
            start += 1
        while end > start and nums[end] == sorted_nums[end]:
            end -= 1

        return end - start + 1
# @lc code=end

