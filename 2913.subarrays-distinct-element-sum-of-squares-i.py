#
# @lc app=leetcode id=2913 lang=python3
#
# [2913] Subarrays Distinct Element Sum of Squares I
#

# @lc code=start
from typing import List


class Solution:
    def sumCounts(self, nums: List[int]) -> int:
        ans, n = 0, len(nums)
        for i in range(n):
            s = set()
            for j in range(i, n):
                s.add(nums[j])
                ans += len(s) * len(s)
        return ans
# @lc code=end

