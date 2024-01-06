#
# @lc app=leetcode id=1582 lang=python3
#
# [1582] Special Positions in a Binary Matrix
#

# @lc code=start
from typing import List


class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        m = len(mat)
        n = len(mat[0])
        ans = 0
        rowOnes = [0] * m
        colOnes = [0] * n

        for i in range(m):
            for j in range(n):
                if mat[i][j] == 1:
                    rowOnes[i] += 1
                    colOnes[j] += 1

        for i in range(m):
            for j in range(n):
                if mat[i][j] == 1 and rowOnes[i] == 1 and colOnes[j] == 1:
                    ans += 1

        return ans
# @lc code=end

