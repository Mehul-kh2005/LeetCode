class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n=len(temperatures)
        lst=[]
        result=[0]*(n)

        for i in range(n):
            while lst and temperatures[i]>temperatures[lst[-1]]:
                idx=lst.pop()
                result[idx]=i-idx
            lst.append(i)

        return result