class Solution:
    def countPairs(self, deliciousness: List[int]) -> int:
        MOD = 10**9 + 7
        count_map = defaultdict(int)
        count = 0
        
        for d in deliciousness:
            for i in range(22):  # Powers of 2 from 2^0 to 2^21
                power_of_two = 1 << i
                complement = power_of_two - d
                if complement in count_map:
                    count = (count + count_map[complement]) % MOD
            
            count_map[d] += 1
        
        return count