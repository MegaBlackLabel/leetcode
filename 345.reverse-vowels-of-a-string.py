#
# @lc app=leetcode id=345 lang=python3
#
# [345] Reverse Vowels of a String
#


# @lc code=start
class Solution:
    def reverseVowels(self, s: str) -> str:
        s_list = list(s)

        vowels = []

        for i, val in enumerate(s_list):
            if val in ["a", "o", "e", "i", "u", "A", "O", "E", "I", "U"]:
                vowels.append((i, val))

        for j in range(len(vowels) // 2):
            s_list[vowels[j][0]] = vowels[len(vowels) - j - 1][1]
            s_list[vowels[len(vowels) - j - 1][0]] = vowels[j][1]

        return "".join(s_list)


# @lc code=end
