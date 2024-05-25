class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        memo={}
        word_set=set(wordDict)
        
        def wordBreakHelper(s,start,word_set,memo):
            if start in memo:
                return memo[start]
            
            valid_substr=[]

            if start==len(s):
                valid_substr.append("")
            
            for end in range(start+1,len(s)+1):
                prefix=s[start:end]
                if prefix in word_set:
                    suffixes=wordBreakHelper(s,end,word_set,memo)
                    for suffix in suffixes:
                        valid_substr.append(prefix+("" if suffix=="" else " ")+suffix)
            
            memo[start]=valid_substr
            return valid_substr
        
        return wordBreakHelper(s,0,word_set,memo)