class Solution:
    def intToRoman(self, num: int) -> str:
        values = [1000, 900, 500, 400, 100, 90,50, 40, 10, 9, 5, 4, 1]
        symbols = ["M", "CM", "D", "CD", "C", "XC","L", "XL", "X", "IX", "V", "IV", "I"]
        result = ""
        while num != 0:
            for i in range(len(values)):
                while num >= values[i]:
                    times = num // values[i]
                    for j in range(times):
                        num = num - values[i]
                        result = result + symbols[i]
        return result
                        
                    
