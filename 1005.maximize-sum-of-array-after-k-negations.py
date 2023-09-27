#
# @lc app=leetcode id=1005 lang=python3
#
# [1005] Maximize Sum Of Array After K Negations
#

# @lc code=start
from typing import List


class Solution:
    def largestSumAfterKNegations(self, nums: List[int], k: int) -> int:
        nums.sort()

        for i, num in enumerate(nums):
            if num > 0 or k == 0:
                break
            nums[i] = -num
            k -= 1

        return sum(nums) - (k % 2) * min(nums) * 2
# @lc code=end

