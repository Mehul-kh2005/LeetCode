# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def numComponents(self, head: Optional[ListNode], nums: List[int]) -> int:
        if head is None:
            return 0
        
        nums_set = set(nums)
        connected_components = 0
        in_component = False
        
        while head:
            if head.val in nums_set:
                if not in_component:
                    connected_components += 1
                    in_component = True
            else:
                in_component = False
            
            head = head.next
        
        return connected_components