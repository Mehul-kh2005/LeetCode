class Solution:
    def firstCompleteIndex(self, arr: List[int], mat: List[List[int]]) -> int:
        num_rows,num_cols=len(mat),len(mat[0])
        row_count=[0]*num_rows
        col_count=[0]*num_cols
        freq={}

        for i in range(num_rows):
            for j in range(num_cols):
                freq[mat[i][j]]=[i,j]

        for num in arr:
            row,col=freq[num]
            row_count[row]+=1
            col_count[col]+=1

            if row_count[row]==num_cols or col_count[col]==num_rows:
                return arr.index(num)