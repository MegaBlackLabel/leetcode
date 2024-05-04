#
# @lc app=leetcode id=2194 lang=python3
#
# [2194] Cells in a Range on an Excel Sheet
#

# @lc code=start
from typing import List


class Solution:
    def cellsInRange(self, s: str) -> List[str]:
        ans = []
        startCol, startRow, _, endCol, endRow = s

        for j in range(ord(startCol), ord(endCol) + 1):
            for i in range(int(startRow), int(endRow) + 1):
                ans.append(chr(j) + str(i))

        return ans
# @lc code=end

