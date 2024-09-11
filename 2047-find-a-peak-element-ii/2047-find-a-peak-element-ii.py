class Solution:
    def findPeakGrid(self, mat: List[List[int]]) -> List[int]:
        dict1={}

        for i in range(len(mat)):
            ele=max(mat[i])
            idx=mat[i].index(ele)
            dict1[ele]=(i,idx)

        return dict1[max(dict1)]