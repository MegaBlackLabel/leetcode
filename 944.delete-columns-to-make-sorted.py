#
# @lc app=leetcode id=944 lang=python3
#
# [944] Delete Columns to Make Sorted
#

# @lc code=start
from typing import List


class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        if not strs or not strs[0]:
            return 0
        num_cols, num_rows = len(strs[0]), len(strs)
        num_remove = 0
        for col_index in range(num_cols):
            for row_index in range(num_rows):
                if row_index > 0 and strs[row_index][col_index] < strs[row_index-1][col_index]:
                    num_remove += 1
                    break
        return num_remove
# @lc code=end

