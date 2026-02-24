#
# @lc app=leetcode id=3042 lang=python3
#
# [3042] Count Prefix and Suffix Pairs I
#

# @lc code=start
from typing import List


class Solution:
    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        count = 0
        for i in range(len(words)):
            for j in range(i + 1, len(words)):
                str1 = words[i]
                str2 = words[j]
                
                if str2.startswith(str1) and str2.endswith(str1):
                    count += 1
        return count
# @lc code=end

