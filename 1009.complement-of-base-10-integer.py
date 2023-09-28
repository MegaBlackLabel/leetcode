#
# @lc app=leetcode id=1009 lang=python3
#
# [1009] Complement of Base 10 Integer
#

# @lc code=start
class Solution:
    def bitwiseComplement(self, n: int) -> int:
        mask = 1
        while mask < n:
            mask = (mask << 1) + 1
        return mask ^ n
# @lc code=end

