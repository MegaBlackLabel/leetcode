#
# @lc app=leetcode id=3105 lang=python3
#
# [3105] Longest Strictly Increasing or Strictly Decreasing Subarray
#

# @lc code=start
from typing import List


class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        max_len = 1
        inc_len = 1
        dec_len = 1
        
        for i in range(1, len(nums)):
            if nums[i] > nums[i-1]:
                inc_len += 1
                dec_len = 1
            elif nums[i] < nums[i-1]:
                dec_len += 1
                inc_len = 1
            else:
                # 等しい場合は増加・減少の連続が途切れる
                inc_len = 1
                dec_len = 1
            
            max_len = max(max_len, inc_len, dec_len)
            
        return max_len
# @lc code=end

