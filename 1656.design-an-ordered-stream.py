#
# @lc app=leetcode id=1656 lang=python3
#
# [1656] Design an Ordered Stream
#

# @lc code=start
from typing import List


class OrderedStream:

    def __init__(self, n: int):
        self.values = [''] * n
        self.i = 0 

    def insert(self, idKey: int, value: str) -> List[str]:
        idKey -= 1  # Converts to 0-indexed.
        self.values[idKey] = value
        if idKey > self.i:
            return []
        while self.i < len(self.values) and self.values[self.i]:
            self.i += 1
        return self.values[idKey:self.i]


# Your OrderedStream object will be instantiated and called as such:
# obj = OrderedStream(n)
# param_1 = obj.insert(idKey,value)
    
# @lc code=end

