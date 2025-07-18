#
# @lc app=leetcode id=529 lang=python3
#
# [529] Minesweeper
#

# @lc code=start
from typing import List


class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        
        def dfs(r, c):
            if r < 0 or r >= len(board) or c < 0 or c >= len(board[0]) or board[r][c] != 'E':
                return
            
            mine_count = 0
            for dr in [-1, 0, 1]:
                for dc in [-1, 0, 1]:
                    if dr == 0 and dc == 0:
                        continue
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < len(board) and 0 <= nc < len(board[0]) and board[nr][nc] == 'M':
                        mine_count += 1
            
            if mine_count > 0:
                board[r][c] = str(mine_count)
            else:
                board[r][c] = 'B'
                for dr in [-1, 0, 1]:
                    for dc in [-1, 0, 1]:
                        dfs(r + dr, c + dc)

        r, c = click
        if board[r][c] == 'M':
            board[r][c] = 'X'
        else:
            dfs(r, c)
        
        return board
# @lc code=end

