class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        rows = len(text1)   # how many letters text1 has
        cols = len(text2)   # how many letters text2 has

        # Build the notebook: (rows+1) x (cols+1), all zeros.
        # Row 0 and column 0 stay 0 (the "empty string" case).
        dp = [[0] * (cols + 1) for _ in range(rows + 1)]

        # i = letters used from text1, j = letters used from text2.
        # Start at 1 because row 0 / column 0 are already correct.
        for i in range(1, rows + 1):
            for j in range(1, cols + 1):

                # Compare the NEWEST letter of each prefix.
                # (The i-th letter is at index i-1.)
                if text1[i - 1] == text2[j - 1]:
                    # Match: take the diagonal answer and add 1
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    # No match: best of "drop from text1" (above)
                    # or "drop from text2" (left)
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

        # Bottom-right cell = all of text1 vs all of text2
        return dp[rows][cols]