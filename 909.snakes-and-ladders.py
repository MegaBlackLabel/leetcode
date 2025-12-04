#
# @lc app=leetcode id=909 lang=python3
#
# [909] Snakes and Ladders
#

# @lc code=start
from typing import List


class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        
        n = len(board)
        moves = [-1] * (n * n)

        idx = 0
        left_to_right = True
        for r in range(n - 1, -1, -1):
            if left_to_right:
                for c in range(n):
                    if board[r][c] != -1:
                        moves[idx] = board[r][c] - 1
                    idx += 1
            else:
                for c in range(n - 1, -1, -1):
                    if board[r][c] != -1:
                        moves[idx] = board[r][c] - 1
                    idx += 1
            left_to_right = not left_to_right

        from collections import deque

        queue = deque([0])
        visited = set()
        visited.add(0)
        steps = 0

        while queue:
            size = len(queue)
            for _ in range(size):
                curr = queue.popleft()
                if curr == n * n - 1:
                    return steps
                for die in range(1, 7):
                    next_pos = curr + die
                    if next_pos < n * n:
                        if moves[next_pos] != -1:
                            next_pos = moves[next_pos]
                        if next_pos not in visited:
                            visited.add(next_pos)
                            queue.append(next_pos)
            steps += 1

        return -1
# @lc code=end

