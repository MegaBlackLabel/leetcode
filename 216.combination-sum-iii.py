#
# @lc app=leetcode id=216 lang=python3
#
# [216] Combination Sum III
#

# @lc code=start
from typing import List


class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        ans = []

        def dfs(k: int, n: int, s: int, path: list[int]) -> None:
            if k == 0 and n == 0:
                ans.append(path)
                return
            if k == 0 or n < 0:
                return

            for i in range(s, 10):
                dfs(k - 1, n - i, i + 1, path + [i])

        dfs(k, n, 1, [])
    
        return ans
# @lc code=end

