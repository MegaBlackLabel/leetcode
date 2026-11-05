#
# @lc app=leetcode id=1324 lang=python3
#
# [1324] Print Words Vertically
#

# @lc code=start
class Solution:
    def printVertically(self, s: str) -> List[str]:
        words = s.split()
      
        max_length = max(len(word) for word in words)
      
        result = []
      
        for col_index in range(max_length):
            current_column = []
            for word in words:
                if col_index < len(word):
                    current_column.append(word[col_index])
                else:
                    current_column.append(' ')
          
            while current_column and current_column[-1] == ' ':
                current_column.pop()
          
            result.append(''.join(current_column))
      
        return result

# @lc code=end

