import sys
class Solution:
    def reverse(self, x: int) -> int:
        r = 0
        while x != 0:
            r = r * 10 + x % 10
            x //= 10
        return r
        
if __name__ == "__main__":
    n = -1534236469
    o = Solution()
    x = o.reverse(n)
    print(x)