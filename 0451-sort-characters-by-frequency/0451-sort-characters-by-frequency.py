class Solution:
    def frequencySort(self, s: str) -> str:
        freq=Counter(s)
        sorted_dict=dict(sorted(freq.items(),key=lambda item:item[1],reverse=True))
        string=""

        for char,value in sorted_dict.items():
            string+=(char)*value

        return string