#
# @lc app=leetcode id=1640 lang=python3
#
# [1640] Check Array Formation Through Concatenation
#

# @lc code=start
from typing import List


class Solution:
    def canFormArray(self, arr: List[int], pieces: List[List[int]]) -> bool:
        concatenated = []
        startToPiece = {piece[0]: piece for piece in pieces}

        for a in arr:
            concatenated += startToPiece.get(a, [])

        return concatenated == arr
# @lc code=end

