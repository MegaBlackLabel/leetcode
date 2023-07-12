#
# @lc app=leetcode id=392 lang=python3
#
# [392] Is Subsequence
#

# @lc code=start


class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        pre = cur = 0
        while pre < len(s) and cur < len(t):
            if s[pre] == t[cur]:
                pre += 1
            cur += 1
        return pre == len(s)


# @lc code=end
