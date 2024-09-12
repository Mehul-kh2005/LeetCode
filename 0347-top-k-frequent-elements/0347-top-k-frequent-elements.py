from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq=Counter(nums)
        freq=dict(sorted(freq.items(),key=lambda item:item[1],reverse=True))
        result=[]

        for num,value in freq.items():
            if k!=0:
                result.append(num)
                k-=1
            else:
                break

        return result