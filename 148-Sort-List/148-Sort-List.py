# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head
            
        lst=[]
        while head is not None:
            lst.append(head.val)
            head=head.next

        lst.sort()

        dummy=ListNode()
        current=dummy

        for value in lst:
            current.next=ListNode(value)
            current=current.next

        return dummy.next