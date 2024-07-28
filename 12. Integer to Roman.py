class Solution:
    def intToRoman(self, num: int) -> str:
        roman_numerals = [
        ("M", 1000),
        ("CM", 900),
        ("D", 500),
        ("CD", 400),
        ("C", 100),
        ("XC", 90),
        ("L", 50),
        ("XL", 40),
        ("X", 10),
        ("IX", 9),
        ("V", 5),
        ("IV", 4),
        ("I", 1)
    ] 
        result = ""                            #For Final output storing
        for symbol, value in roman_numerals:   #running the for loop for geting one by one 
            while num >= value:                #checking the value grater than or equla to num
                result += symbol               #storing the symbal into a result
                num -= value                   # then subracting the value we stored in result
        return result                          #the loop will go until num = 0 , then we print the result