#
# @lc app=leetcode id=481 lang=python3
#
# [481] Magical String
#

# @lc code=start
class Solution:
    def magicalString(self, n: int) -> int:
        
        s = [' ', '1', '2', '2']

        for i in range(3, n + 1):
            if i % 2 == 1:
                s.extend(['1'] * (int(s[i])))
            else:
                s.extend(['2'] * (int(s[i])))

        return sum(1 for c in s[:n + 1] if c == '1')
# @lc code=end

