class Solution(object):
    #s is a string
    #return an int
    def romanToInt(self, s):
        if not 1 <= len(s) <= 15:
            return "Not a valid roman numeral"
        
        total = 0
        values = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        replace_pairs = {"IV": "IIII", 
                        "IX": "VIIII", 
                        "XL": "XXXX",
                        "XC": "LXXXX",
                        "CD": "CCCC", 
                        "CM": "DCCCC"}
        
        for old, new in replace_pairs.items():
            s = s.replace(old, new)

        for curr_letter in s:
            total += values[curr_letter]
        
        if not 1 <= total <= 3999:
            return "Not a valid roman numeral" 
        return total


        