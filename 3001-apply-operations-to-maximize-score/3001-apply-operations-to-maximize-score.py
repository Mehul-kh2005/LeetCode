class Solution:
    MOD = int(1e9 + 7)

    def maximumScore(self, nums: List[int], k: int) -> int:
        n = len(nums)
        prime_scores = [0] * n

        # Find the maximum element in nums to determine the range for prime generation
        max_element = max(nums)

        # Get all prime numbers up to max_element using the Sieve of Eratosthenes
        primes = self.get_primes(max_element)

        # Calculate the prime score for each number in nums
        for index in range(n):
            num = nums[index]

            # Iterate over the generated primes to count unique prime factors
            for prime in primes:
                if prime * prime > num:
                    break  # Stop early if prime^2 exceeds num
                if num % prime != 0:
                    continue  # Skip if the prime is not a factor

                prime_scores[index] += 1  # Increment prime score for the factor
                while num % prime == 0:
                    num //= prime  # Remove all occurrences of this factor

            # If num is still greater than 1, it is a prime number itself
            if num > 1:
                prime_scores[index] += 1

        # Initialize next and previous dominant index arrays
        next_dominant = [n] * n
        prev_dominant = [-1] * n

        # Stack to store indices for a monotonic decreasing prime score
        decreasing_prime_score_stack = deque()

        # Calculate the next and previous dominant indices for each number
        for index in range(n):
            # While the stack is not empty and the current prime score is
            # greater than the stack's top, update next_dominant
            while (
                decreasing_prime_score_stack
                and prime_scores[decreasing_prime_score_stack[-1]]
                < prime_scores[index]
            ):
                top_index = decreasing_prime_score_stack.pop()

                # Set the next dominant element for the popped index
                next_dominant[top_index] = index

            # If the stack is not empty, set the previous dominant element for
            # the current index
            if decreasing_prime_score_stack:
                prev_dominant[index] = decreasing_prime_score_stack[-1]

            # Push the current index onto the stack
            decreasing_prime_score_stack.append(index)

        # Calculate the number of subarrays in which each element is dominant
        num_of_subarrays = [
            (next_dominant[i] - i) * (i - prev_dominant[i]) for i in range(n)
        ]

        # Sort elements in decreasing order based on their values
        sorted_array = sorted(enumerate(nums), key=lambda x: -x[1])

        score = 1

        # Helper function to compute the power of a number modulo MOD
        def _power(base, exponent):
            res = 1

            # Calculate the exponentiation using binary exponentiation
            while exponent > 0:
                # If the exponent is odd, multiply the result by the base
                if exponent % 2:
                    res = (res * base) % self.MOD

                # Square the base and halve the exponent
                base = (base * base) % self.MOD
                exponent //= 2

            return res

        processing_index = 0

        # Process elements while there are operations left
        while k > 0:
            # Get the element with the maximum value
            index, num = sorted_array[processing_index]
            processing_index += 1

            # Calculate the number of operations to apply on the current
            # element
            operations = min(k, num_of_subarrays[index])

            # Update the score by raising the element to the power of
            # operations
            score = (score * _power(num, operations)) % self.MOD

            # Reduce the remaining operations count
            k -= operations

        return score

    # Function to generate prime numbers up to a given limit using the Sieve of Eratosthenes
    def get_primes(self, limit: int) -> List[int]:
        is_prime = [True] * (limit + 1)
        primes = []

        # Start marking from the first prime number (2)
        for number in range(2, limit + 1):
            if not is_prime[number]:
                continue

            # Store the prime number
            primes.append(number)

            # Mark multiples of the prime number as non-prime
            for multiple in range(number * number, limit + 1, number):
                is_prime[multiple] = False

        return primes