#
# @lc app=leetcode id=1117 lang=python3
#
# [1117] Building H2O
#

# @lc code=start
from threading import Semaphore


class H2O:
    def __init__(self):
        self.hydrogen_semaphore = Semaphore(2)
        self.oxygen_semaphore = Semaphore(0)
        self.hydrogen_count = 0

    def hydrogen(self, releaseHydrogen: Callable[[], None]) -> None:
        """
        Method called by hydrogen threads.
        Two hydrogen threads must combine with one oxygen thread to form H2O.
        """
        self.hydrogen_semaphore.acquire()
      
        releaseHydrogen()
      
        self.hydrogen_count += 1
      
        if self.hydrogen_count == 2:
            self.hydrogen_count = 0
            self.oxygen_semaphore.release()

    def oxygen(self, releaseOxygen: Callable[[], None]) -> None:
        """
        Method called by oxygen threads.
        One oxygen thread must wait for two hydrogen threads before forming H2O.
        """
        self.oxygen_semaphore.acquire()
      
        releaseOxygen()
      
        self.hydrogen_semaphore.release()
        self.hydrogen_semaphore.release()
# @lc code=end

