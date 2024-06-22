#
# @lc app=leetcode id=2441 lang=python3
#
# [2441] Largest Positive Integer That Exists With Its Negative
#

# @lc code=start
from typing import List


class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        ans = -1
        seen = set()

        for num in nums:
            if -num in seen:
                ans = max(ans, abs(num))
            else:
                seen.add(num)

        return ans
# @lc code=end

