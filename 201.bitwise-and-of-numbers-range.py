#
# @lc app=leetcode id=201 lang=python3
#
# [201] Bitwise AND of Numbers Range
#

# @lc code=start
class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        return self.rangeBitwiseAnd(left >> 1, right >> 1) << 1 if left < right else left
# @lc code=end

