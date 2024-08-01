class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class MyLinkedList:
    def __init__(self):
        self.head = None        

    def get(self, index: int) -> int:
        temp = self.head
        for _ in range(index):
            if temp is None:
                return -1
            temp = temp.next
        return -1 if temp is None else temp.val

    def addAtHead(self, val: int) -> None:
        new_node = ListNode(val, self.head)
        self.head = new_node

    def addAtTail(self, val: int) -> None:
        new_node = ListNode(val)
        if not self.head:
            self.head = new_node
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new_node

    def addAtIndex(self, index: int, val: int) -> None:
        if index < 0:
            return
        if index == 0:
            self.addAtHead(val)
            return
        new_node = ListNode(val)
        temp = self.head
        for _ in range(index - 1):
            if temp is None:
                return
            temp = temp.next
        if temp is None:
            return
        new_node.next = temp.next
        temp.next = new_node

    def deleteAtIndex(self, index: int) -> None:
        if index < 0:
            return
        if index == 0:
            if self.head:
                self.head = self.head.next
            return
        temp = self.head
        for _ in range(index - 1):
            if temp is None:
                return
            temp = temp.next
        if temp is None or temp.next is None:
            return
        temp.next = temp.next.next