# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        if not head or not head.next:
            return head

        lst=[]
        temp=head
        while temp is not None:
            lst.append(temp.val)
            temp=temp.next

        n=len(lst)
        mid=n//2
        list1=lst[:mid]
        list2=lst[-1:mid-1:-1]
        max_sum=0

        for i in range(mid):
            max_sum=max(max_sum,list1[i]+list2[i])

        return max_sum