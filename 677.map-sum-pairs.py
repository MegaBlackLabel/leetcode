#
# @lc app=leetcode id=677 lang=python3
#
# [677] Map Sum Pairs
#

# @lc code=start
class MapSum:

    def __init__(self):
        
        """
        Initialize your data structure here.
        """
        self.map = {}
        self.prefix_sum = {}

    def insert(self, key: str, val: int) -> None:
        if key in self.map:
            delta = val - self.map[key]
        else:
            delta = val
        self.map[key] = val

        # Update prefix sums
        for i in range(1, len(key) + 1):
            prefix = key[:i]
            self.prefix_sum[prefix] = self.prefix_sum.get(prefix, 0) + delta

    def sum(self, prefix: str) -> int:
        return self.prefix_sum.get(prefix, 0)
        


# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)
# @lc code=end

