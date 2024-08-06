class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []

        digit_to_char = {
            '2': 'abc', '3': 'def', '4': 'ghi',
            '5': 'jkl', '6': 'mno', '7': 'pqrs',
            '8': 'tuv', '9': 'wxyz'
        }

        def backtrack(start,path):
            if start==len(digits):
                result.append(path[:])
                return
            
            for char in digit_to_char[digits[start]]:
                backtrack(start+1,path+char)

        result=[]
        backtrack(0,"")

        return result