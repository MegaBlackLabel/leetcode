#
# @lc app=leetcode id=318 lang=python3
#
# [318] Maximum Product of Word Lengths
#

# @lc code=start
from typing import List

class Solution:
    def maxProduct(self, words: List[str]) -> int:
        n = len(words)
        masks = [0] * n
        lens = [0] * n
        for i in range(n):
            for c in words[i]:
                masks[i] |= 1 << (ord(c) - ord('a'))
            lens[i] = len(words[i])
        max_product = 0
        for i in range(n):
            for j in range(i+1, n):
                if masks[i] & masks[j] == 0:
                    max_product = max(max_product, lens[i] * lens[j])
        return max_product
# @lc code=end

