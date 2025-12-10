#
# @lc app=leetcode id=918 lang=python3
#
# [918] Maximum Sum Circular Subarray
#

# @lc code=start
from typing import List


class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        
        total = 0
        max_sum = float('-inf')
        cur_max = 0
        min_sum = float('inf')
        cur_min = 0

        for num in nums:
            total += num

            cur_max += num
            max_sum = max(max_sum, cur_max)
            if cur_max < 0:
                cur_max = 0

            cur_min += num
            min_sum = min(min_sum, cur_min)
            if cur_min > 0:
                cur_min = 0

        if max_sum > 0:
            return max(max_sum, total - min_sum)
        else:
            return max_sum
# @lc code=end

