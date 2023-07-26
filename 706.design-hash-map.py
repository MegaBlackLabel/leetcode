#
# @lc app=leetcode id=706 lang=python3
#
# [706] Design HashMap
#

# @lc code=start
class MyHashMap:

    def __init__(self):
        self.maps = [[] for _ in range(1000)]


    def put(self, key: int, value: int) -> None:
        index = self.hash(key)
        self.remove(key)
        self.maps[index].append([key, value])


    def get(self, key: int) -> int:
        index = self.hash(key)
        for k, v in self.maps[index]:
            if k == key:
                return v
        return -1
        

    def remove(self, key: int) -> None:
        index = self.hash(key)
        for k, v in self.maps[index]:
            if k == key:
                self.maps[index].remove([k, v])
                break


    def hash(self, key):
        return key % 1000

# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)
# @lc code=end

