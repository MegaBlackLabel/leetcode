#
# @lc app=leetcode id=342 lang=python3
#
# [342] Power of Four
#


# @lc code=start
class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        return n > 0 and bin(n).count("1") == 1 and (n - 1) % 3 == 0


# @lc code=end
