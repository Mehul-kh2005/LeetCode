# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or not head.next or k==0:
            return head
        
        lst=[]
        temp=head
        while temp is not None:
            lst.append(temp.val)
            temp=temp.next

        k=k%len(lst)
        while k!=0:
            lst.insert(0,lst.pop())
            k-=1

        dummy=ListNode()
        head=dummy
        for ele in lst:
            head.next=ListNode(ele)
            head=head.next

        return dummy.next