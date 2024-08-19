#
# @lc app=leetcode id=2744 lang=python3
#
# [2744] Find Maximum Number of String Pairs
#

# @lc code=start
import string
from typing import List


class Solution:
    def maximumNumberOfStringPairs(self, words: List[str]) -> int:
        ans = 0
        seen = [False] * (26 * 26)

        def val(c: str) -> int:
            return string.ascii_lowercase.index(c)

        for word in words:
            if seen[val(word[1]) * 26 + val(word[0])]:
                ans += 1
            seen[val(word[0]) * 26 + val(word[1])] = True

        return ans
# @lc code=end

