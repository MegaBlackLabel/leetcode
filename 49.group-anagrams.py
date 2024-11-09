#
# @lc app=leetcode id=49 lang=python3
#
# [49] Group Anagrams
#

# @lc code=start
import collections
from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = collections.defaultdict(list)
      
        for s in strs:
            key = "".join(sorted(s))
            anagrams[key].append(s)
      

        return list(anagrams.values())
# @lc code=end

