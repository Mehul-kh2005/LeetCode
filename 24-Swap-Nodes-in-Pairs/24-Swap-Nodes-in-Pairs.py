# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        temp = ListNode(0)
        temp.next = head
        prev = temp
        curr = head

        while curr and curr.next:
            next_pair = curr.next.next
            second = curr.next

            # Swap the nodes
            second.next = curr
            curr.next = next_pair
            prev.next = second

            # Move prev and curr pointers forward
            prev = curr
            curr = next_pair
        
        return temp.next