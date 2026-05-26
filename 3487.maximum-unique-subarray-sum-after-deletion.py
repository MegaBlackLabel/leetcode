#
# @lc app=leetcode id=3487 lang=python3
#
# [3487] Maximum Unique Subarray Sum After Deletion
#

# @lc code=start
from typing import List


class Solution:
    def maxSum(self, nums: List[int]) -> int:
        if max(nums) <= 0:
            return max(nums)
    
        unique_positives = set()
        for num in nums:
            if num > 0:
                unique_positives.add(num)
            
        return sum(unique_positives)
# @lc code=end

