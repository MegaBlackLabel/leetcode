#
# @lc app=leetcode id=3349 lang=python3
#
# [3349] Adjacent Increasing Subarrays Detection I
#

# @lc code=start
from typing import List


class Solution:
    def hasIncreasingSubarrays(self, nums: List[int], k: int) -> bool:
        if k == 1:
            return len(nums) >= 2

        max_k_found = 0
        prev_len = 0
        curr_len = 1
        
        for i in range(len(nums) - 1):
            if nums[i] < nums[i + 1]:
                curr_len += 1
            else:
                max_k_found = max(max_k_found, curr_len // 2, min(prev_len, curr_len))
                prev_len = curr_len
                curr_len = 1
        
        max_k_found = max(max_k_found, curr_len // 2, min(prev_len, curr_len))
        
        return max_k_found >= k
# @lc code=end

