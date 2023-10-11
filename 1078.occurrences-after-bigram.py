#
# @lc app=leetcode id=1078 lang=python3
#
# [1078] Occurrences After Bigram
#

# @lc code=start
from typing import List


class Solution:
    def findOcurrences(self, text: str, first: str, second: str) -> List[str]:
        words = text.split()
        return [c for a, b, c in zip(words, words[1:], words[2:]) if a == first and b == second]
# @lc code=end

