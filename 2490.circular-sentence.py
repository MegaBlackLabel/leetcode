#
# @lc app=leetcode id=2490 lang=python3
#
# [2490] Circular Sentence
#

# @lc code=start
class Solution:
    def isCircularSentence(self, sentence: str) -> bool:
        for i, c in enumerate(sentence):
            if c == ' ' and sentence[i - 1] != sentence[i + 1]:
                return False
    
        return sentence[0] == sentence[-1]
# @lc code=end

