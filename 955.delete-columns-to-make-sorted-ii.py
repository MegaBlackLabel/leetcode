#
# @lc app=leetcode id=955 lang=python3
#
# [955] Delete Columns to Make Sorted II
#

# @lc code=start
from typing import List


class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        
        n = len(strs)
        m = len(strs[0])
        deleted = 0
        sorted_pairs = [False] * (n - 1)

        for col in range(m):
            need_delete = False
            for row in range(n - 1):
                if not sorted_pairs[row] and strs[row][col] > strs[row + 1][col]:
                    need_delete = True
                    break

            if need_delete:
                deleted += 1
            else:
                for row in range(n - 1):
                    if strs[row][col] < strs[row + 1][col]:
                        sorted_pairs[row] = True

        return deleted
# @lc code=end

