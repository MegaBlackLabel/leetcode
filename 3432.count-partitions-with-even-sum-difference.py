#
# @lc app=leetcode id=3432 lang=python3
#
# [3432] Count Partitions with Even Sum Difference
#

# @lc code=start
from typing import List


class Solution:
    def countPartitions(self, nums: List[int]) -> int:
        if sum(nums) % 2 == 0:
            return len(nums) - 1
        return 0
# @lc code=end

