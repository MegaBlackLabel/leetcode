#
# @lc app=leetcode id=1880 lang=python3
#
# [1880] Check if Word Equals Summation of Two Words
#

# @lc code=start
class Solution:
    def isSumEqual(self, firstWord: str, secondWord: str, targetWord: str) -> bool:
        first = self._getNumber(firstWord)
        second = self._getNumber(secondWord)
        target = self._getNumber(targetWord)
        
        return first + second == target

    def _getNumber(self, word: str) -> int:
        num = 0
        for c in word:
            num = num * 10 + (ord(c) - ord('a'))
        return num
# @lc code=end

