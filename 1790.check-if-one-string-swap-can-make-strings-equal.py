#
# @lc app=leetcode id=1790 lang=python3
#
# [1790] Check if One String Swap Can Make Strings Equal
#

# @lc code=start
class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        if len(s1) == len(s2):
            temp = []
            for i in range(len(s1)):
                if s1[i] != s2[i]:
                    temp.append(i)
            if len(temp) > 2 or len(temp) == 1:
                return False
            elif len(temp) == 2:
                if s1[temp[0]] == s2[temp[1]] and s1[temp[1]] == s2[temp[0]]:
                    return True
                else:
                    return False
            else:
                return True           
        else:
            return False
# @lc code=end

