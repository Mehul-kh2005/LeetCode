# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if not head or left == right:
            return head

        # Dummy node to simplify edge cases
        dummy = ListNode(0)
        dummy.next = head
        prev = dummy

        # Step 1: Reach the node just before the left position
        for _ in range(left - 1):
            prev = prev.next

        # Step 2: Reverse the segment from left to right
        reverse = None
        curr = prev.next
        for _ in range(right - left + 1):
            next_node = curr.next
            curr.next = reverse
            reverse = curr
            curr = next_node

        # Step 3: Reconnect the reversed segment
        prev.next.next = curr
        prev.next = reverse

        return dummy.next