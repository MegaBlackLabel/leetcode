#
# @lc app=leetcode id=2022 lang=python3
#
# [2022] Convert 1D Array Into 2D Array
#

# @lc code=start
from typing import List


class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        if len(original) != m * n:
            return []

        ans = [[0] * n for _ in range(m)]

        for i, num in enumerate(original):
            ans[i // n][i % n] = num

        return ans
# @lc code=end

