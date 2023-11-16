#
# @lc app=leetcode id=1337 lang=python3
#
# [1337] The K Weakest Rows in a Matrix
#

# @lc code=start
from typing import List


class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        candidates = []

        for i, row in enumerate(mat):
            candidates.append([sum(row), i])

        candidates.sort(key=lambda c: (c[0], c[1]))

        return [i for _, i in candidates[:k]]
# @lc code=end

