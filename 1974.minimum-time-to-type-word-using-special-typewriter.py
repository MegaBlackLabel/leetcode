#
# @lc app=leetcode id=1974 lang=python3
#
# [1974] Minimum Time to Type Word Using Special Typewriter
#

# @lc code=start
class Solution:
    def minTimeToType(self, word: str) -> int:
        moves = 0
        letter = 'a'

        for c in word:
            diff = abs(ord(c) - ord(letter))
            moves += min(diff, 26 - diff)
            letter = c

        return moves + len(word)
# @lc code=end

