#
# @lc app=leetcode id=2423 lang=python3
#
# [2423] Remove Letter To Equalize Frequency
#

# @lc code=start
import collections


class Solution:
    def equalFrequency(self, word: str) -> bool:
        count = collections.Counter(word)

        for c in word:
            count[c] -= 1
            if count[c] == 0:
                del count[c]
            if min(count.values()) == max(count.values()):
                return True
            count[c] += 1

        return False
# @lc code=end

