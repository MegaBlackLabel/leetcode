#
# @lc app=leetcode id=2451 lang=python3
#
# [2451] Odd String Difference
#

# @lc code=start
import collections
from typing import List


class Solution:
    def oddString(self, words: List[str]) -> str:
        def getDiff(s: str) -> List[int]:
            return [ord(b) - ord(a) for a, b in zip(s, s[1:])]

        wordAndDiffTuples = [(word, tuple(getDiff(word))) for word in words]
        diffTupleCount = collections.Counter()

        for _, diffTuple in wordAndDiffTuples:
            diffTupleCount[diffTuple] += 1

        for word, diffTuple in wordAndDiffTuples:
            if diffTupleCount[diffTuple] == 1:
                return word
# @lc code=end

