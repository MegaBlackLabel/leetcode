#
# @lc app=leetcode id=858 lang=python3
#
# [858] Mirror Reflection
#

# @lc code=start
class Solution:
    def mirrorReflection(self, p: int, q: int) -> int:
        while p % 2 == 0 and q % 2 == 0:
            p //= 2
            q //= 2

        if p % 2 == 0:
            return 2
        if q % 2 == 0:
            return 0
        return 1
    
# @lc code=end

