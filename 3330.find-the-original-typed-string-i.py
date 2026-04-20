#
# @lc app=leetcode id=3330 lang=python3
#
# [3330] Find the Original Typed String I
#

# @lc code=start
class Solution:
    def possibleStringCount(self, word: str) -> int:
        ans = 1
        for i in range(1, len(word)):
            # 前の文字と同じなら、追加の可能性を1つ増やす
            if word[i] == word[i-1]:
                ans += 1
        return ans
# @lc code=end

