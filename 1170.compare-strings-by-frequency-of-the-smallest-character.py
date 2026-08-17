#
# @lc app=leetcode id=1170 lang=python3
#
# [1170] Compare Strings by Frequency of the Smallest Character
#

# @lc code=start
import bisect


class Solution:
    def numSmallerByFrequency(self, queries: List[str], words: List[str]) -> List[int]:
        def f(s: str) -> int:
            return s.count(min(s))
        
        words_freq = sorted([f(w) for w in words])
        total_words = len(words)
        
        ans = []
        for q in queries:
            q_freq = f(q)
            idx = bisect.bisect_right(words_freq, q_freq)
            ans.append(total_words - idx)

        return ans
# @lc code=end

