#
# @lc app=leetcode id=1662 lang=python3
#
# [1662] Check If Two String Arrays are Equivalent
#

# @lc code=start
from typing import List


class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        i = 0  
        j = 0 
        a = 0  
        b = 0 

        while i < len(word1) and j < len(word2):
            if word1[i][a] != word2[j][b]:
                return False
            a += 1
            if a == len(word1[i]):
                i += 1
                a = 0
            b += 1
            if b == len(word2[j]):
                j += 1
                b = 0

        return i == len(word1) and j == len(word2)
# @lc code=end

