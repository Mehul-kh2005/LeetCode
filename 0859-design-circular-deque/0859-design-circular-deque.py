class MyCircularDeque:

    def __init__(self, k: int):
        self.deque=[0]*k
        self.front=0
        self.rear=-1
        self.count=0
        self.k=k


    def insertFront(self, value: int) -> bool:
        if self.count<self.k:
            self.front=(self.front+self.k-1)%self.k
            self.deque[self.front]=value
            self.count+=1
            return True

        return False


    def insertLast(self, value: int) -> bool:
        if self.count<self.k:
            self.rear=(self.rear+1)%self.k
            self.deque[self.rear]=value
            self.count+=1
            return True
            
        return False
            

    def deleteFront(self) -> bool:
        if self.count>0:
            self.front=(self.front+1)%self.k
            self.count-=1
            return True
            
        return False


    def deleteLast(self) -> bool:
        if self.count>0:
            self.rear=(self.rear+self.k-1)%self.k
            self.count-=1
            return True
            
        return False


    def getFront(self) -> int:
        if self.count>0:
            return self.deque[self.front]
        return -1
        

    def getRear(self) -> int:
        if self.count>0:
            return self.deque[self.rear]
        return -1


    def isEmpty(self) -> bool:
        return self.count==0


    def isFull(self) -> bool:
        return self.count==self.k


# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()