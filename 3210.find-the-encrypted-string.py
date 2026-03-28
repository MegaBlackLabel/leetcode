#
# @lc app=leetcode id=3210 lang=python3
#
# [3210] Find the Encrypted String
#

# @lc code=start
class Solution:
    def getEncryptedString(self, s: str, k: int) -> str:
        n = len(s)
        k %= n
        return s[k:] + s[0:k]
# @lc code=end

