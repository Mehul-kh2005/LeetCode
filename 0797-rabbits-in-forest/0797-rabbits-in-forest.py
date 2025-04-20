from collections import Counter
import math

class Solution:
    def numRabbits(self, answers:List[int])->int:
        count = Counter(answers)
        total = 0

        for x, freq in count.items():
            group_size = x + 1
            groups = math.ceil(freq / group_size)
            total += groups * group_size

        return total