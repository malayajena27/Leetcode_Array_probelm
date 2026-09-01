class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        m = len(digits)
        n = m - 1
        res = 0
        
        for i in range(m):
            res = res + (digits[i] * (10 ** n))
            n = n - 1
        
        res = res + 1
        
        l = []
        while res > 0:
            l.append(res % 10)
            res = res // 10
        
        l.reverse()
        return l