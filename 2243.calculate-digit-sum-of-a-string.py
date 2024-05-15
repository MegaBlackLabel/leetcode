#
# @lc app=leetcode id=2243 lang=python3
#
# [2243] Calculate Digit Sum of a String
#

# @lc code=start
class Solution:
    def digitSum(self, s: str, k: int) -> str:
        while len(s) > k:
            next = []
            for i in range(0, len(s), k):
                summ = 0
                for j in range(i, min(len(s), i + k)):
                    summ += ord(s[j]) - ord('0')
                next.append(str(summ))
            s = ''.join(next)
        
        return s

# @lc code=end

