#
# @lc app=leetcode id=833 lang=python3
#
# [833] Find And Replace in String
#

# @lc code=start
from typing import List


class Solution:
    def findReplaceString(self, s: str, indices: List[int], sources: List[str], targets: List[str]) -> str:
        
        replacements = sorted(
            [(i, src, tgt) for i, src, tgt in zip(indices, sources, targets)],
            reverse=True
        )

        for i, src, tgt in replacements:
            if s.startswith(src, i):
                s = s[:i] + tgt + s[i + len(src):]

        return s
# @lc code=end

