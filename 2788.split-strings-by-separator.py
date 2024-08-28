#
# @lc app=leetcode id=2788 lang=python3
#
# [2788] Split Strings by Separator
#

# @lc code=start
from typing import List


class Solution:
    def splitWordsBySeparator(self, words: List[str], separator: str) -> List[str]:
        return [splitWord
            for word in words
            for splitWord in word.split(separator)
            if splitWord]
    
# @lc code=end

