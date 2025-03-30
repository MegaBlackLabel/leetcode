#
# @lc app=leetcode id=380 lang=python3
#
# [380] Insert Delete GetRandom O(1)
#

# @lc code=start
class RandomizedSet:

    def __init__(self):
        self.vals = []
        self.val_set = {}

    def insert(self, val: int) -> bool:
        
        if val in self.val_set:
            return False
        self.vals.append(val)
        self.val_set[val] = len(self.vals) - 1
        return True

    def remove(self, val: int) -> bool:
        
        if val not in self.val_set:
            return False
        last_element = self.vals[-1]
        idx_to_remove = self.val_set[val]
        self.vals[idx_to_remove] = last_element
        self.val_set[last_element] = idx_to_remove
        self.vals.pop()
        del self.val_set[val]
        return True

    def getRandom(self) -> int:
        
        import random
        return random.choice(self.vals)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
# @lc code=end

