# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        length = 0
        counter = 0
        node = head
        
        # First pass: determine the length of the list and find the k-th node from the beginning
        while node is not None:
            length += 1
            counter += 1
            if counter == k:
                left = node  # k-th node from the beginning
            node = node.next
        
        # Second pass: find the k-th node from the end
        right = head
        for _ in range(length - k):
            right = right.next
        
        # Swap the values of the k-th node from the beginning and the end
        if left and right:
            left.val, right.val = right.val, left.val
        
        return head