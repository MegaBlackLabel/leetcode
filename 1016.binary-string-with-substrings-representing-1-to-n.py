#
# @lc app=leetcode id=1016 lang=python3
#
# [1016] Binary String With Substrings Representing 1 To N
#

# @lc code=start
class Solution:
    def queryString(self, s: str, n: int) -> bool:
        if n > 1511:
            return False

        for i in range(n, n // 2, -1):
            if format(i, 'b') not in s:
                return False

        return True
# @lc code=end

