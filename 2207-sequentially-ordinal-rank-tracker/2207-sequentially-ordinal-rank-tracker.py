from sortedcontainers import SortedList

class SORTracker:

    def __init__(self):
        self.list=SortedList()
        self.i=0

    def add(self, name: str, score: int) -> None:
        self.list.add([-score,name])

    def get(self) -> str:
        ans=self.list[self.i][1]
        self.i+=1
        return ans

# Your SORTracker object will be instantiated and called as such:
# obj = SORTracker()
# obj.add(name,score)
# param_2 = obj.get()