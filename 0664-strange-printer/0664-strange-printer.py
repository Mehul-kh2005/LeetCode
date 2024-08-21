class Solution:
    def strangePrinter(self, s: str) -> int:
        # Preprocess the string to remove consecutive duplicate characters
        s = "".join(char for char, _ in itertools.groupby(s))
        n = len(s)

        # min_turns[i][j] represents the minimum number of turns to print s[i] to s[j]
        min_turns = [[0] * n for _ in range(n)]

        # Initialize base case
        for i in range(n):
            # It takes 1 turn to print a single character
            min_turns[i][i] = 1

        # Fill the dp table
        for length in range(2, n + 1):
            for start in range(n - length + 1):
                end = start + length - 1

                # Initialize with worst case: print each character separately
                min_turns[start][end] = length

                # Try all possible splits and find the minimum
                for split in range(length - 1):
                    total_turns = (
                        min_turns[start][start + split]
                        + min_turns[start + split + 1][end]
                    )

                    # If the characters at the split and end match, we can save one turn
                    if s[start + split] == s[end]:
                        total_turns -= 1

                    min_turns[start][end] = min(
                        min_turns[start][end], total_turns
                    )

        # Return the minimum turns needed to print the entire string
        return min_turns[0][n - 1] if n > 0 else 0