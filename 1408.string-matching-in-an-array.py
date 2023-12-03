#
# @lc app=leetcode id=1408 lang=python3
#
# [1408] String Matching in an Array
#

# @lc code=start
from typing import List


class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        ans = []
        for a in words:
            for b in words:
                if len(a) < len(b) and b.find(a) != -1:
                    ans.append(a)
                    break
        return ans
# @lc code=end

