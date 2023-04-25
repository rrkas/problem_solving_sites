class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        # Initialize a table to store whether a substring is a palindrome
        table = [[False] * n for _ in range(n)]
        # Initialize the maximum length seen so far
        max_len = 0
        # Initialize variables to keep track of the indices of the longest palindrome seen so far
        start, end = 0, 0
        # Iterate over the table diagonally
        for k in range(n):
            i, j = 0, k
            while j < n:
                # If the substring has length 1 or 2 and is a palindrome, mark it as a palindrome
                if j - i < 2:
                    table[i][j] = s[i] == s[j]
                # If the substring has length greater than 2 and the characters at the ends match and the substring without the ends is a palindrome, mark it as a palindrome
                else:
                    table[i][j] = s[i] == s[j] and table[i + 1][j - 1]
                # If the substring is a palindrome and its length is greater than the maximum length seen so far, update the maximum length and the indices of the longest palindrome seen so far
                if table[i][j] and j - i + 1 > max_len:
                    max_len = j - i + 1
                    start, end = i, j
                # Move to the next substring
                i += 1
                j += 1
        return s[start : end + 1]
