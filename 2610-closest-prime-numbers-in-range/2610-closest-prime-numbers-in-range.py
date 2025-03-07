class Solution:
    def isPrime(self, num):
        if num < 2:
            return False
        if num == 2 or num == 3:
            return True
        if num % 2 == 0:
            return False
        divisor = 3
        while divisor * divisor <= num:
            if num % divisor == 0:
                return False
            divisor += 2
        return True

    def closestPrimes(self, left, right):
        prev_prime = -1
        closestA = -1
        closestB = -1
        min_difference = float("inf")

        for candidate in range(left, right + 1):
            if self.isPrime(candidate):
                if prev_prime != -1:
                    difference = candidate - prev_prime
                    if difference < min_difference:
                        min_difference = difference
                        closestA = prev_prime
                        closestB = candidate
                    if difference == 1 or difference == 2:
                        return [prev_prime, candidate]
                prev_prime = candidate

        return [closestA, closestB] if closestA != -1 else [-1, -1]