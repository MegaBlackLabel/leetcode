#
# @lc app=leetcode id=1859 lang=python3
#
# [1859] Sorting the Sentence
#

# @lc code=start
class Solution:
    def sortSentence(self, s: str) -> str:
        return ' '.join([w[:-1] for w in sorted(s.split(), key=lambda x: x[-1])])
# @lc code=end

