#
# @lc app=leetcode id=2269 lang=python3
#
# [2269] Find the K-Beauty of a Number
#

# @lc code=start
class Solution:
    def divisorSubstrings(self, num: int, k: int) -> int:
        s = str(num)
        ans = 0

        for i in range(len(s) - k + 1):
            x = int(s[i:i + k])
            if x != 0 and num % x == 0:
                ans += 1

        return ans
    
# @lc code=end

