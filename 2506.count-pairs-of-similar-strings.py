#
# @lc app=leetcode id=2506 lang=python3
#
# [2506] Count Pairs Of Similar Strings
#

# @lc code=start
from typing import List


class Solution:
    def similarPairs(self, words: List[str]) -> int:
        return sum(set(words[i]) == set(words[j])
               for i in range(len(words))
               for j in range(i + 1, len(words)))
# @lc code=end

