#
# @lc app=leetcode id=2273 lang=python3
#
# [2273] Find Resultant Array After Removing Anagrams
#

# @lc code=start
import collections
from typing import List


class Solution:
    def removeAnagrams(self, words: List[str]) -> List[str]:
        ans = []

        def isAnagram(a: str, b: str) -> bool:
            count = collections.Counter(a)
            count.subtract(collections.Counter(b))
            
            return all(value == 0 for value in count.values())

        i = 0
        while i < len(words):
            j = i + 1
            while j < len(words) and isAnagram(words[i], words[j]):
                j += 1
            ans.append(words[i])
            i = j

        return ans
# @lc code=end

