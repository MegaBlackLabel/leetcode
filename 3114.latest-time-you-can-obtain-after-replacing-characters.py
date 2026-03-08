#
# @lc app=leetcode id=3114 lang=python3
#
# [3114] Latest Time You Can Obtain After Replacing Characters
#

# @lc code=start
class Solution:
    def findLatestTime(self, s: str) -> str:
        
        ans = list(s)

        if ans[0] == '?':
            ans[0] = '1' if ans[1] == '?' or ans[1] < '2' else '0'
        
        if ans[1] == '?':
            ans[1] = '1' if ans[0] == '1' else '9'

        if ans[3] == '?':
            ans[3] = '5'
        
        if ans[4] == '?':
            ans[4] = '9'

        return "".join(ans)
# @lc code=end

