#
# @lc app=leetcode id=1160 lang=python3
#
# [1160] Find Words That Can Be Formed by Characters
#

# @lc code=start
import collections
from typing import List


class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        ans = 0
        count = collections.Counter(chars)

        for word in words:
            tempCount = count.copy()
            for c in word:
                tempCount[c] -= 1
                if tempCount[c] < 0:
                    ans -= len(word)
                    break
            ans += len(word)

        return ans
# @lc code=end

