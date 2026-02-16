class Solution:
    def reverseBits(self, n: int) -> int:
        def rev(v: int, length: int) -> int:
            if length == 1:
                return v & 1

            half = length >> 1
            mask = (1 << half) - 1

            lo = v & mask
            hi = v >> half

            return (rev(lo, half) << half) | rev(hi, half)

        return rev(n, 32)