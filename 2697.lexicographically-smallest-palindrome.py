#
# @lc app=leetcode id=2697 lang=python3
#
# [2697] Lexicographically Smallest Palindrome
#

# @lc code=start
class Solution:
    def makeSmallestPalindrome(self, s: str) -> str:
        chars = list(s)
        i = 0
        j = len(s) - 1

        while i < j:
            minChar = min(chars[i], chars[j])
            chars[i] = minChar
            chars[j] = minChar
            i += 1
            j -= 1

        return ''.join(chars)
# @lc code=end

