# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, root: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        cur = root
        N = 0
        while cur:
            N += 1
            cur = cur.next
        
        # Calculate the size of each part and the number of parts that need an extra node
        width, remainder = divmod(N, k)
        
        # Prepare the result list
        ans = []
        cur = root
        for i in range(k):
            # Initialize a dummy node for the current part
            head = write = ListNode(None)
            # Append nodes to the current part
            for _ in range(width + (i < remainder)):
                write.next = write = ListNode(cur.val)
                if cur:
                    cur = cur.next
            # Append the head of the current part to the result list
            ans.append(head.next)
        
        return ans