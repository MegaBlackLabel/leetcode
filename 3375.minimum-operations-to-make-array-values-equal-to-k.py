#
# @lc app=leetcode id=3375 lang=python3
#
# [3375] Minimum Operations to Make Array Values Equal to K
#

# @lc code=start
from typing import List


class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        unique_nums = set(nums)
        
        if min(unique_nums) < k:
            return -1

        return len(unique_nums) - 1 if k in unique_nums else len(unique_nums)
# @lc code=end

