# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def spiralMatrix(self, m: int, n: int, head: Optional[ListNode]) -> List[List[int]]:
        i=j=0
        curr_d=0
        directions=[[0,1],[1,0],[0,-1],[-1,0]]

        matrix=[[-1]*n for _ in range(m)]

        while head is not None:
            matrix[i][j]=head.val

            new_i=i+directions[curr_d][0]
            new_j=j+directions[curr_d][1]

            if (
                new_i>=m or
                new_j>=n or
                matrix[new_i][new_j]!=-1
            ):
                curr_d=(curr_d+1)%4
            i+=directions[curr_d][0]
            j+=directions[curr_d][1]

            head=head.next

        return matrix