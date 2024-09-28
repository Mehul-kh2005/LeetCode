class MyCircularQueue:

    def __init__(self, k: int):
        self.queue=[0]*k
        self.front=0
        self.rear=-1
        self.count=0
        self.size=k

    def enQueue(self, value: int) -> bool:
        if self.count<self.size:
            self.rear=(self.rear+1)%self.size
            self.queue[self.rear]=value
            self.count+=1
            return True
        return False

    def deQueue(self) -> bool:
        if self.count>0:
            self.front=(self.front+1)%self.size
            self.count-=1
            return True
        return False

    def Front(self) -> int:
        if self.count>0:
            return self.queue[self.front]
        return -1

    def Rear(self) -> int:
        if self.count>0:
            return self.queue[self.rear]
        return -1

    def isEmpty(self) -> bool:
        return self.count==0

    def isFull(self) -> bool:
        return self.count==self.size


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()