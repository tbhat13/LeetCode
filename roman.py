class Solution(object):
    #s is a string
    #return an int
    def romanToInt(self, s):
        total = 0
        values = {"I" : 1, "V" : 5, "X" : 10, "L" : 50, "C" : 100, "D" : 500, "M" : 1000}
        for elem in s:
            print(values[elem])
            
        