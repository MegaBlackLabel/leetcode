#
# @lc app=leetcode id=524 lang=python3
#
# [524] Longest Word in Dictionary through Deleting
#

# @lc code=start
from typing import List


class Solution:
    def findLongestWord(self, s: str, dictionary: List[str]) -> str:
        
        def is_subsequence(word: str) -> bool:
            it = iter(s)
            return all(char in it for char in word)

        dictionary.sort(key=lambda x: (-len(x), x))
        for word in dictionary:
            if is_subsequence(word):
                return word
        return ""
# @lc code=end

