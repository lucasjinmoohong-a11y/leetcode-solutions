"""
Approach:
Store values of roman numerals in a dictionary. Convert the input into a list and enumerate it. 
For each place value of the number, implement additive and subtractive forms of roman numerals and
pull roman numerals from the dictionary using the place value. Add these roman numerals to the 
output string and then return the string. 

Time Complexity:  O(log(n))
Space Complexity: O(log(n))

Tests:
3749 --> "MMMDCCXLIX"
58 --> "LVIII"
1994 --> "MCMXCIV"

All tests passed
"""

class Solution:
    def intToRoman(self, num):
        romans = {
            '1' : 'I',
            '5' : 'V', 
            '10' : 'X',
            '50' : 'L',
            '100' : 'C',
            '500' : 'D', 
            '1000' : 'M'
        }
        list = []
        for x in str(num):
            list.append(x)

        output = ''
        for index, value in enumerate(list):
            while True:
                if int(value) < 4:
                    for y in range(int(value)):
                        output+=romans[str(pow(10,len(list)-index-1))]
                    break
                elif int(value) == 4 or int(value) == 5:
                    for y in range(5-int(value)):
                        output+=romans[str(pow(10,len(list)-index-1))]
                    output+=romans[str(5*(pow(10,len(list)-index-1)))]
                    break
                elif int(value) < 9:
                    output+=romans[str(5*(pow(10,len(list)-index-1)))]
                    value = str(int(value)-5)
                elif int(value) == 9:
                    output+=romans[str(pow(10,len(list)-index-1))]
                    output+=romans[str((pow(10,len(list)-index)))]
                    break
        return output

if __name__ == "__main__":
    sol = Solution()
    print(sol.intToRoman())
