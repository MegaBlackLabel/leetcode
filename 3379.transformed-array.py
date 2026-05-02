#
# @lc app=leetcode id=3379 lang=python3
#
# [3379] Transformed Array
#

# @lc code=start
from typing import List


class Solution:
    def constructTransformedArray(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [0] * n
        
        for i in range(n):
            new_idx = (i + nums[i]) % n
            res[i] = nums[new_idx]
            
        return res
# @lc code=end

