#
# @lc app=leetcode id=386 lang=python3
#
# [386] Lexicographical Numbers
#

# @lc code=start
from typing import List


class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        
        def dfs(num: int):
            if num > n:
                return
            ans.append(num)
            for i in range(10):
                dfs(num * 10 + i)

        ans = []
        for i in range(1, 10):
            dfs(i)
        return ans
# @lc code=end

