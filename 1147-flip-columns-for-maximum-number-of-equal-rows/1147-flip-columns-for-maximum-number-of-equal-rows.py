class Solution:
    def maxEqualRowsAfterFlips(self, matrix: List[List[int]]) -> int:
        patternFrequency={}

        for currentRow in matrix:
            patternBuilder="".join('T' if currentRow[0]==num else 'F' for num in currentRow)

            patternFrequency[patternBuilder]=patternFrequency.get(patternBuilder,0)+1

        return max(patternFrequency.values())