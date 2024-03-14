#
# @lc app=leetcode id=1935 lang=python3
#
# [1935] Maximum Number of Words You Can Type
#

# @lc code=start
class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        ans = 0
        broken = set(brokenLetters)

        for word in text.split():
            ans += all(c not in broken for c in word)

        return ans
# @lc code=end

