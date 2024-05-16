#
# @lc app=leetcode id=2248 lang=python3
#
# [2248] Intersection of Multiple Arrays
#

# @lc code=start
from typing import List


class Solution:
    def intersection(self, nums: List[List[int]]) -> List[int]:
        count = [0] * 1001

        for A in nums:
            for a in A:
                count[a] += 1

        return [i for i, c in enumerate(count) if c == len(nums)]
# @lc code=end

