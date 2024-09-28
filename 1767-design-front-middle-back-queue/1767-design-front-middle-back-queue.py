class FrontMiddleBackQueue:

    def __init__(self):
        self.array = []

    def pushFront(self, val: int) -> None:
        self.array.insert(0, val)  

    def pushMiddle(self, val: int) -> None:
        mid = len(self.array) // 2  
        self.array.insert(mid, val)  

    def pushBack(self, val: int) -> None:
        self.array.append(val)  

    def popFront(self) -> int:
        if self.array:
            return self.array.pop(0)  
        return -1

    def popMiddle(self) -> int:
        if self.array:
            mid = (len(self.array) - 1) // 2  
            return self.array.pop(mid) 
        return -1

    def popBack(self) -> int:
        if self.array:
            return self.array.pop()  
        return -1



# Your FrontMiddleBackQueue object will be instantiated and called as such:
# obj = FrontMiddleBackQueue()
# obj.pushFront(val)
# obj.pushMiddle(val)
# obj.pushBack(val)
# param_4 = obj.popFront()
# param_5 = obj.popMiddle()
# param_6 = obj.popBack()