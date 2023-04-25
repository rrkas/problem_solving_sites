class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        res = ""
        for i in range(n):
            for j in range(i + 1, n + 1):
                t = s[i:j]
                if t == t[::-1] and len(t) > len(res):
                    res = t
        return res


# fails for time limit exceeded
