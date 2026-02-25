class Solution:
    def frequencySort(self, s: str) -> str:
        hash_map={}

        for ch in s:
            hash_map[ch]=hash_map.get(ch,0)+1

        hash_map=sorted(hash_map.items(),key=lambda x:x[1],reverse=True)

        return "".join(key*value for key,value in hash_map)