#
# @lc app=leetcode id=1941 lang=python3
#
# [1941] Check if All Characters Have Equal Number of Occurrences
#

# @lc code=start
import collections


class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        return len(set(collections.Counter(s).values())) == 1
# @lc code=end

