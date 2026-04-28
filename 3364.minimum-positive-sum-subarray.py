#
# @lc app=leetcode id=3364 lang=python3
#
# [3364] Minimum Positive Sum Subarray 
#

# @lc code=start
from typing import List


class Solution:
    def minimumSumSubarray(self, nums: List[int], l: int, r: int) -> int:
        n = len(nums)
        min_sum = float('inf')
        
        for k in range(l, r + 1):
        
            current_window_sum = sum(nums[:k])
            
            if current_window_sum > 0:
                min_sum = min(min_sum, current_window_sum)
            
            for i in range(k, n):
                current_window_sum += nums[i] - nums[i - k]
                if current_window_sum > 0:
                    min_sum = min(min_sum, current_window_sum)
        
        return min_sum if min_sum != float('inf') else -1
    
# @lc code=end

