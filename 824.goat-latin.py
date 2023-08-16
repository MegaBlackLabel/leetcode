#
# @lc app=leetcode id=824 lang=python3
#
# [824] Goat Latin
#

# @lc code=start
class Solution:
    def toGoatLatin(self, sentence: str) -> str:
        ans = []
        kVowels = 'aeiouAEIOU'

        i = 1
        for word in sentence.split():
            if i > 1:
                ans.append(' ')
            if word[0] in kVowels:
                    ans.append(word)
            else:
                ans.append(word[1:] + word[0])
            ans.append('ma' + 'a' * i)
            i += 1

        return ''.join(ans)
# @lc code=end

