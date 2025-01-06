class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        n=len(boxes)
        result=[0]*n
        balls=operations=0

        for i in range(n):
            result[i]+=operations
            balls+=int(boxes[i])
            operations+=balls

        balls=operations=0

        for i in range(n-1,-1,-1):
            result[i]+=operations
            balls+=int(boxes[i])
            operations+=balls

        return result