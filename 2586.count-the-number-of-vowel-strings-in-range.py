#
# @lc app=leetcode id=2586 lang=python3
#
# [2586] Count the Number of Vowel Strings in Range
#

# @lc code=start
from typing import List


class Solution:
    def vowelStrings(self, words: List[str], left: int, right: int) -> int:
        kVowels = 'aeiou'
        return sum(word[0] in kVowels and word[-1] in kVowels for word in words[left:right + 1])
# @lc code=end

