class Solution:
    def reverse(self, x: int) -> int:
        sign = -1 if x < 0 else 1
        x = abs(x)

        su = 0
        while x != 0:
            d = x % 10
            su = su * 10 + d
            x = x // 10

        su *= sign

        if su < -2**31 or su > 2**31 - 1:
            return 0

        return su