#
# @lc app=leetcode id=522 lang=python3
#
# [522] Longest Uncommon Subsequence II
#

# @lc code=start
from typing import List


class Solution:
    def findLUSlength(self, strs: List[str]) -> int:
        
        def is_subsequence(s1: str, s2: str) -> bool:
            it = iter(s2)
            return all(c in it for c in s1)

        max_length = -1
        for i, s1 in enumerate(strs):
            if all(not is_subsequence(s1, s2) for j, s2 in enumerate(strs) if i != j):
                max_length = max(max_length, len(s1))

        return max_length
# @lc code=end

