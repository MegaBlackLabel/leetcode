#
# @lc app=leetcode id=526 lang=python3
#
# [526] Beautiful Arrangement
#

# @lc code=start
class Solution:
    def countArrangement(self, n: int) -> int:
        
        def count(pos, visited):
            if pos > n:
                return 1
            total = 0
            for i in range(1, n + 1):
                if not visited[i] and (i % pos == 0 or pos % i == 0):
                    visited[i] = True
                    total += count(pos + 1, visited)
                    visited[i] = False
            return total

        visited = [False] * (n + 1)
        return count(1, visited)
# @lc code=end

