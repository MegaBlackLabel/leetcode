#
# @lc app=leetcode id=77 lang=python3
#
# [77] Combinations
#

# @lc code=start
from typing import List


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        ans = []

        def dfs(s: int, path: list[int]) -> None:
            if len(path) == k:
                ans.append(path.copy())
                return

            for i in range(s, n + 1):
                path.append(i)
                dfs(i + 1, path)
                path.pop()

        dfs(1, [])
    
        return ans
# @lc code=end

