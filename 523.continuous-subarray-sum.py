#
# @lc app=leetcode id=523 lang=python3
#
# [523] Continuous Subarray Sum
#

# @lc code=start
from typing import List


class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        
        if len(nums) < 2:
            return False
        
        remainder_map = {0: -1}
        current_sum = 0
        for i, num in enumerate(nums):
            current_sum += num
            
            if k != 0:
                current_sum %= k
            
            if current_sum in remainder_map:
                if i - remainder_map[current_sum] > 1:
                    return True
            else:
                remainder_map[current_sum] = i
        return False

# @lc tags=hash-table;array;prefix-sum
# @lc code=end

