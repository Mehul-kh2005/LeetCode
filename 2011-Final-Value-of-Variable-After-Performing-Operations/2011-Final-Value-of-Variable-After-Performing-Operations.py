class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        result=0
        for char in operations:
            if char=="++X" or char=="X++":
                result+=1
            else:
                result-=1
                
        return result