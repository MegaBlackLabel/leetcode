#
# @lc app=leetcode id=168 lang=python3
#
# [168] Excel Sheet Column Title
#


# @lc code=start
class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        capitals = [chr(x) for x in range(ord("A"), ord("Z") + 1)]

        result = []
        while columnNumber > 0:
            result.append(capitals[(columnNumber - 1) % 26])
            columnNumber = (columnNumber - 1) // 26
        result.reverse()
        return "".join(result)


# @lc code=end
