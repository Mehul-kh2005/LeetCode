# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

from math import gcd

class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head

        prev=head
        curr=head.next
        while curr:
            temp=ListNode(gcd(prev.val,curr.val),curr)
            prev.next=temp
            prev=curr
            curr=curr.next

        return head