# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        result=[-1,-1]

        min_distance=float("inf")

        prev_node=head
        curr_node=head.next
        curr_index=1
        prev_critical_index=0
        first_critical_index=0

        while curr_node.next is not None:
            if (curr_node.val<prev_node.val and curr_node.val<curr_node.next.val) or (curr_node.val>prev_node.val and curr_node.val>curr_node.next.val):

                if prev_critical_index==0:
                    prev_critical_index=curr_index
                    first_critical_index=curr_index
                else:
                    min_distance=min(min_distance,curr_index-prev_critical_index)
                    prev_critical_index=curr_index
            
            curr_index+=1
            prev_node=curr_node
            curr_node=curr_node.next
        
        if min_distance!=float("inf"):
            max_distance=prev_critical_index-first_critical_index
            result=[min_distance,max_distance]
    
        return result