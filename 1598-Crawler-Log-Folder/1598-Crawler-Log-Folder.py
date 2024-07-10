class Solution:
    def minOperations(self, logs: List[str]) -> int:
        counter=0
        for log in logs:
            if log=="../":
                counter -= 1 if counter>0 else 0
            elif log=="./":
                continue
            else:
                counter+=1
        return counter