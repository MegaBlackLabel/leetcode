#
# @lc app=leetcode id=1863 lang=python3
#
# [1863] Sum of All Subset XOR Totals
#

# @lc code=start
from typing import List


class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        def dfs(i: int, xors: int) -> int:
            if i == len(nums):
                return xors

            x = dfs(i + 1, xors)
            y = dfs(i + 1, nums[i] ^ xors)
            return x + y

        return dfs(0, 0)

# @lc code=end

