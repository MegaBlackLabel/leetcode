#
# @lc app=leetcode id=1869 lang=python3
#
# [1869] Longer Contiguous Segments of Ones than Zeros
#

# @lc code=start
class Solution:
    def checkZeroOnes(self, s: str) -> bool:
        longestOnes = 0
        longestZeros = 0
        currentOnes = 0
        currentZeros = 0

        for c in s:
            if c == '0':
                currentOnes = 0
                currentZeros += 1
                longestZeros = max(longestZeros, currentZeros)
            else:
                currentZeros = 0
                currentOnes += 1
                longestOnes = max(longestOnes, currentOnes)

        return longestOnes > longestZeros
# @lc code=end

