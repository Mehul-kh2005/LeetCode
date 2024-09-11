class Solution:
    def findPeakGrid(self, mat: List[List[int]]) -> List[int]:
        left = 0
        right = len(mat) - 1

        while left < right:
            mid = left + (right - left) // 2
            # Find the index of the maximum element in the middle row
            max_idx_mid = mat[mid].index(max(mat[mid]))
            # Find the index of the maximum element in the next row
            max_idx_next = mat[mid + 1].index(max(mat[mid + 1]))

            # Compare the peak values in the current row and the next row
            if mat[mid][max_idx_mid] < mat[mid + 1][max_idx_next]:
                left = mid + 1
            else:
                right = mid

        # Find the index of the peak element in the final row
        peak_idx = mat[left].index(max(mat[left]))
        return [left, peak_idx]