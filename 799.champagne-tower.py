#
# @lc app=leetcode id=799 lang=python3
#
# [799] Champagne Tower
#

# @lc code=start
class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        
        tower = [[0] * (i + 1) for i in range(query_row + 1)]
        tower[0][0] = poured

        for r in range(query_row):
            for c in range(r + 1):
                if tower[r][c] > 1:
                    overflow = (tower[r][c] - 1) / 2
                    tower[r + 1][c] += overflow
                    tower[r + 1][c + 1] += overflow
                    tower[r][c] = 1

        return min(1, tower[query_row][query_glass])
# @lc code=end

