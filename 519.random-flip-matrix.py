#
# @lc app=leetcode id=519 lang=python3
#
# [519] Random Flip Matrix
#

# @lc code=start
from random import randint
from typing import List


class Solution:

    def __init__(self, m: int, n: int):
        
        self.num_rows = m
        self.num_cols = n
        self.total_cells = m * n
        self.flip_map = {}

    def flip(self) -> List[int]:
        self.total_cells -= 1
        x = randint(0, self.total_cells)
        idx = self.flip_map.get(x, x)
        self.flip_map[x] = self.flip_map.get(self.total_cells, self.total_cells)
        return [idx // self.num_cols, idx % self.num_cols]

    def reset(self) -> None:
        self.total_cells = self.num_rows * self.num_cols
        self.flip_map.clear()


# Your Solution object will be instantiated and called as such:
# obj = Solution(m, n)
# param_1 = obj.flip()
# obj.reset()
# @lc code=end

