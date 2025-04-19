#
# @lc app=leetcode id=419 lang=python3
#
# [419] Battleships in a Board
#

# @lc code=start
from typing import List


class Solution:
    def countBattleships(self, board: List[List[str]]) -> int:
        ans = 0

        for i, row in enumerate(board):
            for j, cell in enumerate(row):
                if cell == '.':
                    continue
                if i > 0 and board[i - 1][j] == 'X':
                    continue
                if j > 0 and board[i][j - 1] == 'X':
                    continue
                ans += 1

        return ans
# @lc code=end

