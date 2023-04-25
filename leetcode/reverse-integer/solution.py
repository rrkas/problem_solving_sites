class Solution:
    def reverse(self, x: int) -> int:
        signed = x < 0
        
        if signed:
            x *= -1
        
        r = 0
        while x:
            r = r * 10 + x % 10
            x //= 10
        
        if signed:
            r *= -1
        
        v = 2 ** 31
        # print(r - v, r + v)
        if r > v - 1 or r < -v:
            r = 0
        
        return r
