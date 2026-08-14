class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n < 0:
            x = 1 / x
            n = -n
        if n == 0:
            return 1.0

        s = 1.0

        while n > 0:
            if n % 2 == 1:
                s = s * x

            x = x * x
            n = n // 2

        return s