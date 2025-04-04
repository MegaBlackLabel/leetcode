#
# @lc app=leetcode id=187 lang=python3
#
# [187] Repeated DNA Sequences
#

# @lc code=start
from typing import List


class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        ans = set()
        seen = set()

        for i in range(len(s) - 9):
            seq = s[i:i + 10]
            if seq in seen:
                ans.add(seq)
            seen.add(seq)

        return list(ans)
# @lc code=end

