class Solution:
    def constructDistancedSequence(self, n: int) -> List[int]:
        length=2*n-1
        result=[0]*length
        used=set()

        def backtrack(pos):
            if pos==length:
                return True

            if result[pos]!=0:
                return backtrack(pos+1)

            for num in range(n,0,-1):
                if num in used:
                    continue

                if num==1:
                    result[pos]=1
                    used.add(1)
                    if backtrack(pos+1):
                        return True
                    result[pos]=0
                    used.remove(1)

                else:
                    if pos+num<length and result[pos+num]==0:
                        result[pos]=result[pos+num]=num
                        used.add(num)
                        if backtrack(pos+1):
                            return True
                        result[pos]=result[pos+num]=0
                        used.remove(num)

            return False                 
        
        backtrack(0)
        return result