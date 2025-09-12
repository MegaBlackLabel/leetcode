#
# @lc app=leetcode id=777 lang=python3
#
# [777] Swap Adjacent in LR String
#

# @lc code=start
class Solution:
    def canTransform(self, start: str, result: str) -> bool:
        
        if start.replace("X", "") != result.replace("X", ""):
            return False

        i, j = 0, 0
        n = len(start)

        while i < n and j < n:
            while i < n and start[i] == "X":
                i += 1
            while j < n and result[j] == "X":
                j += 1

            if i < n and j < n:
                if start[i] != result[j]:
                    return False
                if start[i] == "L" and i < j:
                    return False
                if start[i] == "R" and i > j:
                    return False
                i += 1
                j += 1

        return True
# @lc code=end

