class Solution:
    def countAndSay(self, n: int) -> str:
        if n == 1:
            return '1'

        prevString = '1'
    
        for i in range(1, n):
            emptystring = ''
            count = 1

            for j in range(1, len(prevString)):
                if prevString[j] == prevString[j-1]:
                    count += 1
                else:
                    emptystring = emptystring + str(count) + str(prevString[j-1])
                    count = 1

            emptystring = emptystring + str(count) + str(prevString[-1])
            prevString = emptystring

        return prevString