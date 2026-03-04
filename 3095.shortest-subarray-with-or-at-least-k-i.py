#
# @lc app=leetcode id=3095 lang=python3
#
# [3095] Shortest Subarray With OR at Least K I
#

# @lc code=start
from typing import List


class Solution:
    def minimumSubarrayLength(self, nums: List[int], k: int) -> int:
        
        n = len(nums)
        min_len = float('inf')
        
        for i in range(n):
            current_or = 0
            for j in range(i, n):
                current_or |= nums[j]
                if current_or >= k:
                    min_len = min(min_len, j - i + 1)
                    break
        
        return min_len if min_len != float('inf') else -1
# @lc code=end

