#
# @lc app=leetcode id=3452 lang=python3
#
# [3452] Sum of Good Numbers
#

# @lc code=start
from typing import List


class Solution:
    def sumOfGoodNumbers(self, nums: List[int], k: int) -> int:
        total_sum = 0
        n = len(nums)
        
        for i in range(n):
            is_good = True
            
            # Check element at index i - k
            if i - k >= 0:
                if nums[i] <= nums[i - k]:
                    is_good = False
            
            # Check element at index i + k
            if i + k < n:
                if nums[i] <= nums[i + k]:
                    is_good = False
                    
            if is_good:
                total_sum += nums[i]
                
        return total_sum
# @lc code=end

