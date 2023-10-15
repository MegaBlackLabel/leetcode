#
# @lc app=leetcode id=1114 lang=python3
#
# [1114] Print in Order
#

# @lc code=start
from threading import Lock


class Foo:
    def __init__(self):
        self.firstDone = Lock()
        self.secondDone = Lock()
        self.firstDone.acquire()
        self.secondDone.acquire()


    def first(self, printFirst: 'Callable[[], None]') -> None:
        
        # printFirst() outputs "first". Do not change or remove this line.
        printFirst()
        self.firstDone.release()



    def second(self, printSecond: 'Callable[[], None]') -> None:
        
        # printSecond() outputs "second". Do not change or remove this line.
        self.firstDone.acquire()
        printSecond()
        self.secondDone.release()


    def third(self, printThird: 'Callable[[], None]') -> None:
        
        # printThird() outputs "third". Do not change or remove this line.
        self.secondDone.acquire()
        printThird()

# @lc code=end

