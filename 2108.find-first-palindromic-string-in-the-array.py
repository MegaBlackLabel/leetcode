#
# @lc app=leetcode id=2108 lang=python3
#
# [2108] Find First Palindromic String in the Array
#

# @lc code=start
from typing import List


class Solution:
    def firstPalindrome(self, words: List[str]) -> str:
        def isPalindrome(s: str) -> bool:
            i = 0
            j = len(s) - 1
            while i < j:
                if s[i] != s[j]:
                    return False
                i += 1
                j -= 1
            return True
        return next((word for word in words if isPalindrome(word)), '')
# @lc code=end

