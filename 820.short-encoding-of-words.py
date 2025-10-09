#
# @lc app=leetcode id=820 lang=python3
#
# [820] Short Encoding of Words
#

# @lc code=start
from typing import List


class Solution:
    def minimumLengthEncoding(self, words: List[str]) -> int:
        
        words = set(words)
        for word in list(words):
            for i in range(1, len(word)):
                words.discard(word[i:])

        return sum(len(word) + 1 for word in words)
# @lc code=end

