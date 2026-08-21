class Solution:
    def isHappy(self, n: int) -> bool:
        s = 0
        seen = set()

        while n not in seen:
            seen.add(n)
            s = 0

            while n > 0:
                d = n % 10
                s = s + (d * d)
                n = n // 10

            if s == 1:
                return True

            n = s

        return False