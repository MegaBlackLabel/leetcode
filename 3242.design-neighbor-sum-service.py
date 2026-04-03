#
# @lc app=leetcode id=3242 lang=python3
#
# [3242] Design Neighbor Sum Service
#

# @lc code=start
class NeighborSum:

    def __init__(self, grid: list[list[int]]):
        self.grid = grid
        self.n = len(grid)
        self.pos = {}
        # 値の座標を記録 [O(N^2)]
        for r in range(self.n):
            for c in range(self.n):
                self.pos[grid[r][c]] = (r, c)

    def adjacentSum(self, value: int) -> int:
        r, c = self.pos[value]
        res = 0
        # 上下左右の隣接要素
        for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nr, nc = r + dr, c + dc
            if 0 <= nr < self.n and 0 <= nc < self.n:
                res += self.grid[nr][nc]
        return res

    def diagonalSum(self, value: int) -> int:
        r, c = self.pos[value]
        res = 0
        # 斜めの隣接要素
        for dr, dc in [(-1, -1), (-1, 1), (1, -1), (1, 1)]:
            nr, nc = r + dr, c + dc
            if 0 <= nr < self.n and 0 <= nc < self.n:
                res += self.grid[nr][nc]
        return res
        


# Your NeighborSum object will be instantiated and called as such:
# obj = NeighborSum(grid)
# param_1 = obj.adjacentSum(value)
# param_2 = obj.diagonalSum(value)
# @lc code=end

