#
# @lc app=leetcode id=1329 lang=python3
#
# [1329] Sort the Matrix Diagonally
#

# @lc code=start
from collections import defaultdict


class Solution:

  def diagonalSort(self, mat: list[list[int]]) -> list[list[int]]:
    m, n = len(mat), len(mat[0])
    diagonals = defaultdict(list)

    # Group elements by diagonal (row - col is constant)
    for i in range(m):
      for j in range(n):
        diagonals[i - j].append(mat[i][j])

    # Sort each diagonal in descending order so we can pop() from the end in O(1) time
    for k in diagonals:
      diagonals[k].sort(reverse=True)

    # Put the sorted elements back into the matrix
    for i in range(m):
      for j in range(n):
        mat[i][j] = diagonals[i - j].pop()

    return mat
# @lc code=end

