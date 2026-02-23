#
# @lc app=leetcode id=3038 lang=python3
#
# [3038] Maximum Number of Operations With the Same Score I
#

# @lc code=start
from typing import List


class Solution:
    def maxOperations(self, nums: List[int]) -> int:
        
        if len(nums) < 2:
            return 0
        
        target_score = nums[0] + nums[1]
        operations_count = 1  
        
        for i in range(2, len(nums) - 1, 2):
            if nums[i] + nums[i+1] == target_score:
                operations_count += 1
            else:
                break
                
        return operations_count
    # @lc code=end

