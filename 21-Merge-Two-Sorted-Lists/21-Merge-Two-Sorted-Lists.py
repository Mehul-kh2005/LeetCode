# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, head1: Optional[ListNode], head2: Optional[ListNode]) -> Optional[ListNode]:
        if head1 is None :
            return head2
        if head2 is None :
            return head1

        if head1.val<=head2.val:
            mhead=head1
        else:
            mhead=head2
        curr1=mhead.next

        if mhead==head1:
            curr2=head2
        else:
            curr2=head1
        prev=mhead

        while curr1 is not None and curr2 is not None:
            if curr1.val<=curr2.val:
                prev.next=curr1
                prev=curr1
                curr1=curr1.next
            else:
                prev.next=curr2
                prev=curr2
                curr2=curr2.next

        if curr1 is not None:
            prev.next=curr1
        if curr2 is not None:
            prev.next=curr2

        return mhead       