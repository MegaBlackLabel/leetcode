#
# @lc app=leetcode id=1592 lang=python3
#
# [1592] Rearrange Spaces Between Words
#

# @lc code=start
class Solution:
    def reorderSpaces(self, text: str) -> str:
        space_count = text.count(' ')
        words = text.split()
        num_spaces_between_words = len(words) - 1
      
        if num_spaces_between_words == 0:
            return words[0] + ' ' * space_count
      
        spaces_to_distribute = space_count // num_spaces_between_words
        remaining_spaces = space_count % num_spaces_between_words
      
        return (' ' * spaces_to_distribute).join(words) + ' ' * remaining_spaces

# @lc code=end

