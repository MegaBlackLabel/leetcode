#
# @lc app=leetcode id=788 lang=python3
#
# [788] Rotated Digits
#

# @lc code=start
class Solution:
    def rotatedDigits(self, n: int) -> int:
        
        valid = {'0', '1', '8', '2', '5', '6', '9'}
        diff = {'2', '5', '6', '9'}
        ans = 0
        for i in range(1, n + 1):
            s = str(i)
            if all(c in valid for c in s) and any(c in diff for c in s):
                ans += 1
        return ans
# @lc code=end

