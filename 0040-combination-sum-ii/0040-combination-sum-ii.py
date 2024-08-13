class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        def backtrack(start: int, path: List[int], target: int):
            if target == 0:
                result.append(path[:])
                return
            
            for i in range(start, len(candidates)):
                if i > start and candidates[i] == candidates[i - 1]:
                    continue  # Skip duplicates
                if candidates[i] > target:
                    break  # No need to continue if the current number exceeds the target
                
                path.append(candidates[i])
                backtrack(i + 1, path, target - candidates[i])
                path.pop()
        
        candidates.sort()
        result = []
        backtrack(0, [], target)
        return result