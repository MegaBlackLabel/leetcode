#
# @lc app=leetcode id=3411 lang=python3
#
# [3411] Maximum Subarray With Equal Products
#

# @lc code=start
import math
from typing import List


class Solution:
    def maxLength(self, nums: List[int]) -> int:
        n = len(nums)
        max_len = 0
        
        for i in range(n):
            current_prod = 1
            current_gcd = nums[i]
            current_lcm = nums[i]
        
            for j in range(i, n):
                val = nums[j]
                
                current_prod *= val
                current_gcd = math.gcd(current_gcd, val)
                current_lcm = math.lcm(current_lcm, val)
                
                if current_prod == current_gcd * current_lcm:
                    max_len = max(max_len, j - i + 1)
                else:
                    if current_prod > current_gcd * current_lcm:
                        break
                        
        return max_len
# @lc code=end

