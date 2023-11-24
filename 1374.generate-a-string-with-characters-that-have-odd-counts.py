#
# @lc app=leetcode id=1374 lang=python3
#
# [1374] Generate a String With Characters That Have Odd Counts
#

# @lc code=start
class Solution:
    def generateTheString(self, n: int) -> str:
        s = 'a' * n
        if n % 2 == 0:
            s = s[:-1] + 'b'
        return s
# @lc code=end

