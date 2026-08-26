class Solution:
    def romanToInt(self, s: str) -> int:
        symbols = {"M" : 1000, "D" : 500,  "C" : 100, "L" : 50, "X" : 10 , "V":5,  "I":1}
        result = 0
        for i in  range(len(s)):
            if i < len(s)-1 and symbols[s[i]] < symbols[s[i+1]]:
                result = result - symbols[s[i]]
            else:
                result = result + symbols[s[i]]     
        return result       

