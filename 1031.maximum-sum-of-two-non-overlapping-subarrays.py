#
# @lc app=leetcode id=1031 lang=python3
#
# [1031] Maximum Sum of Two Non-Overlapping Subarrays
#

# @lc code=start
from typing import List


class Solution:
    def maxSumTwoNoOverlap(self, nums: List[int], firstLen: int, secondLen: int) -> int:
        def max_sum(L, M):
            prefix_sum = [0] * (len(nums) + 1)
            for i in range(len(nums)):
                prefix_sum[i+1] = prefix_sum[i] + nums[i]
                
            ans = 0
            max_L = 0 
            
            for i in range(L + M, len(prefix_sum)):
                max_L = max(max_L, prefix_sum[i - M] - prefix_sum[i - M - L])
                cur_M = prefix_sum[i] - prefix_sum[i - M]
                ans = max(ans, max_L + cur_M)
                
            return ans

        return max(max_sum(firstLen, secondLen), max_sum(secondLen, firstLen))
# @lc code=end

