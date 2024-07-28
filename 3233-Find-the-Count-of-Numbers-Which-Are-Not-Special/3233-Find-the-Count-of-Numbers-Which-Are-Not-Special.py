primes = [2]
comps = [False]*(10**5+1)

for x in range(3, 10**5, 2):
    if not comps[x]:
        tx = x+x
        primes.append(x)
        while tx <= 10**5:
            comps[tx] = True
            tx += x

class Solution:
    def nonSpecialCount(self, l: int, r: int) -> int:        
        squares = []
        for x in primes:
            squares.append(x*x)
        ans = 0
        for x in squares:
            if x > r:
                break
            ans += x >= l
        return (r - l + 1 ) - ans