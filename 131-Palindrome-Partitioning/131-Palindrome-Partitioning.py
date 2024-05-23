class Solution:
    def partition(self, s: str) -> List[List[str]]:
        def isPalindrome(sub):
            return sub==sub[::-1]
        
        def backtrack(start,path):
            if start==len(s):
                subsets.append(path[:])
                return

            for i in range(start,len(s)):
                currSubstring=s[start:i+1]
                if isPalindrome(currSubstring):
                    path.append(currSubstring)
                    backtrack(i+1,path)
                    path.pop()
        
        subsets=[]
        backtrack(0,[])
        return subsets