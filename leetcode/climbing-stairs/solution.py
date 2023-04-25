class Solution:
    def climbStairs(self, n: int) -> int:
        # Base case: there is only one way to climb 0 or 1 step.
        if n == 0 or n == 1:
            return 1

        # Initialize the memoization table.
        dp = [0] * (n + 1)

        # Set the base cases for the memoization table.
        dp[0] = 1
        dp[1] = 1

        # Fill up the memoization table using the recurrence relation.
        for i in range(2, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2]

        # Return the answer.
        return dp[n]
