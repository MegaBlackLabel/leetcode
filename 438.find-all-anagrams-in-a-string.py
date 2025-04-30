#
# @lc app=leetcode id=438 lang=python3
#
# [438] Find All Anagrams in a String
#

# @lc code=start
from typing import List


class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        
        result = []

        p_count = {}
        for char in p:
            if char in p_count:
                p_count[char] += 1
            else:
                p_count[char] = 1

        s_count = {}
        for i in range(len(p)):
            if i < len(s):
                if s[i] in s_count:
                    s_count[s[i]] += 1
                else:
                    s_count[s[i]] = 1

        if s_count == p_count:
            result.append(0)

        for i in range(len(p), len(s)):
            if s[i] in s_count:
                s_count[s[i]] += 1
            else:
                s_count[s[i]] = 1

            s_count[s[i - len(p)]] -= 1
            if s_count[s[i - len(p)]] == 0:
                del s_count[s[i - len(p)]]

            if s_count == p_count:
                result.append(i - len(p) + 1)

        return result
# @lc code=end

