# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        
        def reverseLinkedList(head,k):
            prev=None
            curr=head
            while k>0:
                next_node=curr.next
                curr.next=prev
                prev=curr
                curr=next_node
                k-=1

            return prev

        count=0
        temp=head
        while temp:
            count+=1
            temp=temp.next

        dummy=ListNode(0,head)
        
        prev_end=dummy
        while count>=k:
            start=prev_end.next
            end=start

            for _ in range(k-1):
                end=end.next

            next_grp=end.next

            end.next=None
            prev_end.next=reverseLinkedList(start,k)

            start.next=next_grp
            prev_end=start
            count-=k

        return dummy.next