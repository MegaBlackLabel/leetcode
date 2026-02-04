#
# @lc app=leetcode id=1006 lang=python3
#
# [1006] Clumsy Factorial
#

# @lc code=start
class Solution:
    def clumsy(self, n: int) -> int:
        
        if n <= 2:
            return n
        if n == 3:
            return 6

        res = n * (n - 1) // (n - 2) + (n - 3)
        n -= 4

        while n >= 4:
            res -= n * (n - 1) // (n - 2)
            res += (n - 3)
            n -= 4

        if n == 3:
            res -= n * (n - 1) // (n - 2)
        elif n == 2:
            res -= n * (n - 1)
        elif n == 1:
            res -= n

        return res
# @lc code=end

