#
# @lc app=leetcode id=821 lang=python3
#
# [821] Shortest Distance to a Character
#

# @lc code=start
from typing import List


class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:
        prev = float('-inf')
        res = []
        for i in range(len(s)):
            if s[i] == c:
                prev = i
            res.append(i-prev)
        
        prev = float('inf')
        for i in range(len(s)-1,-1,-1):
            if s[i] == c:
                prev = i
            res[i] = min(res[i],prev-i)
        
        return res
# @lc code=end

