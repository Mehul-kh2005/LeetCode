# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head

        prev=head
        curr=head.next
        while curr is not None:
            value=gcd(prev.val,curr.val)
            new_node=ListNode(value,curr)
            prev.next=new_node

            prev=curr
            curr=curr.next

        return head