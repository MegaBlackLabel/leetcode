#
# @lc app=leetcode id=2765 lang=python3
#
# [2765] Longest Alternating Subarray
#

# @lc code=start
from typing import List


class Solution:
    def alternatingSubarray(self, nums: List[int]) -> int:
        ans = 1
        dp = 1

        for i in range(1, len(nums)):
            targetDiff = -1 if dp % 2 == 0 else 1
            if nums[i] - nums[i - 1] == targetDiff:
                dp += 1
            elif nums[i] - nums[i - 1] == 1:
                dp = 2
            else:
                dp = 1
            ans = max(ans, dp)

        return -1 if ans == 1 else ans
# @lc code=end

