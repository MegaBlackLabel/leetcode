#
# @lc app=leetcode id=3065 lang=python3
#
# [3065] Minimum Operations to Exceed Threshold Value I
#

# @lc code=start
from typing import List


class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        return sum(num < k for num in nums)


# @lc code=end

