#
# @lc app=leetcode id=1844 lang=python3
#
# [1844] Replace All Digits with Characters
#

# @lc code=start
class Solution:
    def replaceDigits(self, s: str) -> str:
        chars = list(s)

        for i in range(1, len(chars), 2):
            chars[i] = chr(ord(chars[i - 1]) + ord(chars[i]) - ord('0'))

        return ''.join(chars)
# @lc code=end

