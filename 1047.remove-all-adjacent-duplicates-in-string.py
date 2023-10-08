#
# @lc app=leetcode id=1047 lang=python3
#
# [1047] Remove All Adjacent Duplicates In String
#

# @lc code=start
class Solution:
    def removeDuplicates(self, s: str) -> str:
        str = list()

        for c in s:
            if str and str[-1] == c:
                str.pop()
            else:
                str.append(c)

        return "".join(str)
# @lc code=end

