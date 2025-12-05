#
# @lc app=leetcode id=910 lang=python3
#
# [910] Smallest Range II
#

# @lc code=start
from typing import List


class Solution:
    def smallestRangeII(self, nums: List[int], k: int) -> int:
        
        nums.sort()
        n = len(nums)
        res = nums[-1] - nums[0]

        for i in range(n - 1):
            high = max(nums[i] + k, nums[-1] - k)
            low = min(nums[0] + k, nums[i + 1] - k)
            res = min(res, high - low)

        return res
# @lc code=end

