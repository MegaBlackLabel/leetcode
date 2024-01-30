#
# @lc app=leetcode id=1704 lang=python3
#
# [1704] Determine if String Halves Are Alike
#

# @lc code=start
class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        kVowels = 'aeiouAEIOU'
        aVowelsCount = sum(c in kVowels for c in s[:len(s) // 2])
        bVowelsCount = sum(c in kVowels for c in s[len(s) // 2:])
        return aVowelsCount == bVowelsCount
# @lc code=end

