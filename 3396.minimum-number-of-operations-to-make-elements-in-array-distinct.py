#
# @lc app=leetcode id=3396 lang=python3
#
# [3396] Minimum Number of Operations to Make Elements in Array Distinct
#

# @lc code=start
from typing import List


class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        seen = set()
        # Traverse from right to left to find the first duplicate
        for i in range(len(nums) - 1, -1, -1):
            if nums[i] in seen:
                # All elements from index 0 to i must be removed
                # Each operation removes 3 elements
                return i // 3 + 1
            seen.add(nums[i])
        
        # If no duplicates are found, return 0
        return 0
# @lc code=end

