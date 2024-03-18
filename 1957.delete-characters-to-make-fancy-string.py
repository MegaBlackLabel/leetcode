#
# @lc app=leetcode id=1957 lang=python3
#
# [1957] Delete Characters to Make Fancy String
#

# @lc code=start
class Solution:
    def makeFancyString(self, s: str) -> str:
        ans = []
        for c in s:
            if len(ans) < 2 or ans[-1] != c or ans[-2] != c:
                ans.append(c)
        return ''.join(ans)
# @lc code=end

