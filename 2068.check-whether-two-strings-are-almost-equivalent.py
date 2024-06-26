#
# @lc app=leetcode id=2068 lang=python3
#
# [2068] Check Whether Two Strings are Almost Equivalent
#

# @lc code=start
import collections


class Solution:
    def checkAlmostEquivalent(self, word1: str, word2: str) -> bool:
        count = collections.Counter(word1)
        count.subtract(collections.Counter(word2))
        return all(abs(freq) <= 3 for freq in count.values())
# @lc code=end

