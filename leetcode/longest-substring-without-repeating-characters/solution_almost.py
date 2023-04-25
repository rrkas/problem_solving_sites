class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(set(s)) == 1:
            return 1

        maxlen = 0
        n = len(s)
        for i in range(n):
            for j in range(i + 1, n + 1):
                t = s[i:j]
                st = set(t)
                if len(t) == len(st) and len(t) > maxlen:
                    print(t)
                    maxlen = len(t)
        return maxlen


# 1 edge case failed: time limit exceeded
