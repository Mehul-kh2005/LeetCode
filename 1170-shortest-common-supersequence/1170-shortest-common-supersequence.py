class Solution:
    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:
        str1_length = len(str1)
        str2_length = len(str2)

        dp = [
            [0 for _ in range(str2_length + 1)] for _ in range(str1_length + 1)
        ]

        for row in range(str1_length + 1):
            dp[row][0] = row

        for col in range(str2_length + 1):
            dp[0][col] = col

        for row in range(1, str1_length + 1):
            for col in range(1, str2_length + 1):
                if str1[row - 1] == str2[col - 1]:
                    dp[row][col] = dp[row - 1][col - 1] + 1
                else:
                    dp[row][col] = min(dp[row - 1][col], dp[row][col - 1]) + 1

        super_sequence = []
        row, col = str1_length, str2_length

        while row > 0 and col > 0:
            if str1[row - 1] == str2[col - 1]:
                super_sequence.append(str1[row - 1])
                row -= 1
                col -= 1
            elif dp[row - 1][col] < dp[row][col - 1]:
                super_sequence.append(str1[row - 1])
                row -= 1
            else:
                super_sequence.append(str2[col - 1])
                col -= 1

        while row > 0:
            super_sequence.append(str1[row - 1])
            row -= 1
        while col > 0:
            super_sequence.append(str2[col - 1])
            col -= 1

        return "".join(super_sequence[::-1])