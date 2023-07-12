#
# @lc app=leetcode id=409 lang=python3
#
# [409] Longest Palindrome
#

# @lc code=start
from collections import Counter


class Solution:
    def longestPalindrome(self, s: str) -> int:
        ct = Counter(s)
        res = 0
        f = 0
        for v in ct.values():
            if v % 2 == 0:
                res += v
            else:
                res += v - 1
                f = 1
        return res + f


# @lc code=end
