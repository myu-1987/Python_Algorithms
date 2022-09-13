class Solution(object):
    def romanToInt(s):        
        symbol = {"I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000}
        """
        :type s: str
        :rtype: int
        """
        result=0
        for y in range(len(s)-1):
            if symbol[s[y+1]] > symbol[s[y]]:
                result -= symbol[s[y]]
            else:
                result += symbol[s[y]]
        result += symbol[s[len(s)-1]]
        print(result)
        return result


    romanToInt("MCMXCIV")
            
        