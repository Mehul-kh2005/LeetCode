from collections import Counter

class Solution:
    def findEvenNumbers(self, digits: List[int]) -> List[int]:
        result=[]
        freq=Counter(digits)

        for i in range(100,1000,2):
            flag=True
            new_freq=freq.copy()

            for num in str(i):
                if int(num) in new_freq:
                    new_freq[int(num)]-=1

                    if new_freq[int(num)]==0:
                        del new_freq[int(num)]
                else:
                    flag=False
                    break                

            if flag:
                result.append(i)

        return result