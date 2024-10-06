#
# @lc app=leetcode id=3014 lang=python3
#
# [3014] Minimum Number of Pushes to Type Word I
#

import collections

# @lc code=start
class Solution:
    def minimumPushes(self, word: str) -> int:
        freqs = sorted(collections.Counter(word).values(), reverse=True) # type: ignore
        return sum(freq * (i // 8 + 1) for i, freq in enumerate(freqs))
# @lc code=end

