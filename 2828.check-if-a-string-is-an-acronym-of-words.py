#
# @lc app=leetcode id=2828 lang=python3
#
# [2828] Check if a String Is an Acronym of Words
#

# @lc code=start
from typing import List


class Solution:
    def isAcronym(self, words: List[str], s: str) -> bool:
        return (len(words) == len(s) and
            all(word[0] == c for word, c in zip(words, s)))
# @lc code=end

