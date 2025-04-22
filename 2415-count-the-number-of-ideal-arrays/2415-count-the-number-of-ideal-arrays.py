from math import isqrt
MOD = 10**9 + 7

class Solution:
    def idealArrays(self, n: int, maxValue: int) -> int:
        MAX = n + 10000  # safe upper bound
        fact = [1] * (MAX)
        inv_fact = [1] * (MAX)

        for i in range(1, MAX):
            fact[i] = fact[i - 1] * i % MOD

        # Fermat's little theorem to compute inverse
        inv_fact[MAX - 1] = pow(fact[MAX - 1], MOD - 2, MOD)
        for i in range(MAX - 2, 0, -1):
            inv_fact[i] = inv_fact[i + 1] * (i + 1) % MOD

        def comb(a, b):
            if a < b:
                return 0
            return fact[a] * inv_fact[b] % MOD * inv_fact[a - b] % MOD

        res = 0
        for x in range(1, maxValue + 1):
            i = x
            pf = {}  # prime factor -> count
            d = 2
            while d * d <= i:
                while i % d == 0:
                    pf[d] = pf.get(d, 0) + 1
                    i //= d
                d += 1
            if i > 1:
                pf[i] = pf.get(i, 0) + 1

            # Now compute total combinations for this x
            ways = 1
            for exp in pf.values():
                ways = ways * comb(exp + n - 1, exp) % MOD

            res = (res + ways) % MOD

        return res