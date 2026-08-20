#
# @lc app=leetcode id=1186 lang=python3
#
# [1186] Maximum Subarray Sum with One Deletion
#

# @lc code=start
import math


class Solution:
    def maximumSum(self, arr: List[int]) -> int:
        ans = -math.inf
        zero = -math.inf 
        one = -math.inf
        
        for a in arr:
            one = max(a, one + a, zero)
            zero = max(a, zero + a)
            ans = max(ans, one)
            
        return ans
# @lc code=end

