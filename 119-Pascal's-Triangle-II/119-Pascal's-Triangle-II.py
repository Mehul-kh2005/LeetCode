class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        triangle=[[1]]

        for i in range(1,rowIndex+1):
            newRow=[1]
            prevRow=triangle[-1]

            for j in range(1,i):
                newRow.append(prevRow[j-1]+prevRow[j])

            newRow.append(1)

            triangle.append(newRow)
        
        return triangle[rowIndex]