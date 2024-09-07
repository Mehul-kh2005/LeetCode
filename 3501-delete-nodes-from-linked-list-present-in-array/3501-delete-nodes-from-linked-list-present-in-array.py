# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def modifiedList(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:
        nums=set(nums)
        new_head=ListNode(0)
        new_head.next=head
        curr_node=new_head
        
        while curr_node and curr_node.next:
            if curr_node.next.val in nums:
                curr_node.next=curr_node.next.next
            else:
                curr_node=curr_node.next
        
        return new_head.next

        