class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        ans=[0]*len(queries)
        prefix_sum=[0]*len(words)
        vowels={'a','e','i','o','u'}
        sum=0

        for i in range(len(words)):
            current_word=words[i]
            if current_word[0] in vowels and current_word[-1] in vowels:
                sum+=1

            prefix_sum[i]=sum

        for i in range(len(queries)):
            query=queries[i]

            ans[i]=prefix_sum[query[1]] - (0 if query[0]==0 else prefix_sum[query[0]-1])

        return ans