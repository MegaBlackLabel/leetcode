#
# @lc app=leetcode id=693 lang=python3
#
# [693] Binary Number with Alternating Bits
#

# @lc code=start
class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        n = bin(n).replace("0b","")

        for i in range(1,len(n)):
            if n[i]!=n[i-1]:
                pass
            else:
                return False
        else:
            return True
# @lc code=end

