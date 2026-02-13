#
# @lc app=leetcode id=1017 lang=python3
#
# [1017] Convert to Base -2
#

# @lc code=start
class Solution:
    def baseNeg2(self, n: int) -> str:
        
        if n == 0:
            return "0"
        
        res = []
        while n != 0:
            n, r = divmod(n, -2)
            if r < 0:
                r += 2
                n += 1
            res.append(str(r))
        
        return ''.join(reversed(res))
# @lc code=end

