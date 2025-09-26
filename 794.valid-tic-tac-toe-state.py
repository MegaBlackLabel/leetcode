#
# @lc app=leetcode id=794 lang=python3
#
# [794] Valid Tic-Tac-Toe State
#

# @lc code=start
from typing import List


class Solution:
    def validTicTacToe(self, board: List[str]) -> bool:
        
        def win(player: str) -> bool:
            for i in range(3):
                if all(board[i][j] == player for j in range(3)):
                    return True
                if all(board[j][i] == player for j in range(3)):
                    return True
            if all(board[i][i] == player for i in range(3)):
                return True
            if all(board[i][2 - i] == player for i in range(3)):
                return True
            return False

        x_count = sum(row.count('X') for row in board)
        o_count = sum(row.count('O') for row in board)

        if o_count not in {x_count - 1, x_count}:
            return False

        x_win = win('X')
        o_win = win('O')

        if x_win and o_win:
            return False
        if x_win and x_count != o_count + 1:
            return False
        if o_win and x_count != o_count:
            return False

        return True
# @lc code=end

