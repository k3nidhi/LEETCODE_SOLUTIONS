class Solution:
    def romanToInt(self, s: str) -> int:
        hmap = {
            'M' : 1000,
            'D' : 500,
            'C' : 100,
            'L' : 50,
            'X' : 10,
            'V' : 5,
            'I' : 1
        }

        result = 0
        for i in range(length := len(s)):
            if (i < length - 1) and hmap[s[i]] < hmap[s[i+1]]:
                result -= hmap[s[i]]
            else:
                result += hmap[s[i]]

        return result
            
