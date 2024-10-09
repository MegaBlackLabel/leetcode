#
# @lc app=leetcode id=5 lang=python3
#
# [5] Longest Palindromic Substring
#

# @lc code=start
class Solution:
    def longestPalindrome(self, s: str) -> str:
        t = '#'.join('@' + s + '$')
        n = len(t)

        maxExtends = [0] * n
        center = 0

        for i in range(1, n - 1):
            rightBoundary = center + maxExtends[center]
            mirrorIndex = center - (i - center)
            maxExtends[i] = (rightBoundary > i and min(rightBoundary - i, maxExtends[mirrorIndex]))

            while t[i + 1 + maxExtends[i]] == t[i - 1 - maxExtends[i]]:
                maxExtends[i] += 1

            if i + maxExtends[i] > rightBoundary:
                center = i

        maxExtend, bestCenter = max((extend, i)
                                for i, extend in enumerate(maxExtends))
        return s[(bestCenter - maxExtend) // 2:(bestCenter + maxExtend) // 2]
# @lc code=end

