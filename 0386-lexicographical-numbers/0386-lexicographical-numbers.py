class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        result=[]
        current=1

        for _ in range(n):
            result.append(current)

            if current*10<=n:
                current*=10

            else:
                while current%10==9 or current+1>n:
                    current//=10
                current+=1

        return result