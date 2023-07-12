#
# @lc app=leetcode id=171 lang=python3
#
# [171] Excel Sheet Column Number
#


# @lc code=start
class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        res = 0
        for c in columnTitle:
            res = res * 26 + ord(c) - 64
        return res


# @lc code=end
