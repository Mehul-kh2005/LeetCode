from sortedcontainers import SortedDict
from itertools import accumulate

class MyCalendarThree:

    def __init__(self):
        self.event=SortedDict()

    def book(self, startTime: int, endTime: int) -> int:
        self.event[startTime]=self.event.get(startTime,0)+1
        self.event[endTime]=self.event.get(endTime,0)-1

        return max(accumulate(self.event.values()))
       
# Your MyCalendarThree object will be instantiated and called as such:
# obj = MyCalendarThree()
# param_1 = obj.book(startTime,endTime)