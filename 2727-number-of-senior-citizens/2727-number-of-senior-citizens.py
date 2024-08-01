class Solution:
    def countSeniors(self, details: List[str]) -> int:
        count=0
        for passenger in details:
            if int(passenger[11])*10+int(passenger[12])>60:
                count+=1
        return count 