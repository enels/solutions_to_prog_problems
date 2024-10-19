class Solution:
    def intToRoman(self, num: int) -> str:

        result = ""

        special_d = {1: "I", 2: "II", 3: "III", 5: "V", 10: "X", 50: "L", 100: "C", 500: "D", 1000: "M"}

        # check for the basic values
        for k,v in special_d.items():
            if k == num:
                return v
            elif k == num + 1:  # 4 or 9
                part1 = str(special_d[1])
                part2 = str(special_d[num+1])
                return part1+part2
            elif k == num + 10: # 40 or 90
                part1 = str(special_d[10])
                part2 = str(special_d[num+10])
                return part1+part2
            elif k == num + 100: # 400 or 900
                part1 = str(special_d[100])
                part2 = str(special_d[num + 100])
                return part1+part2
            #return part1 + part2
        
        if num > 10 and num < 100:
            ans = num / 10
            rem = num % 10
            # check answer is a special character
            if ans == 4 or ans == 9:
                part1 = str(special_d[1])
                part2 = str(special_d[num+1])
                first_part = part1 + part2
            else:
                first_part = ans * "X"

