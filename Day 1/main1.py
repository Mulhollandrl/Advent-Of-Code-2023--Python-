import re
from enums import SPELLED_OUT_NUMBERS

class Day1:
    def __init__(self, file_path = "c:/Users/Richard/csPersonal/AoC23 Py/Day 1/data/day1part1_input.csv") -> None:
        self.FILE_PATH = file_path
                
    def get_first_last_digits(self, string, spelled=False):
        if spelled:
            # print(string, end="")
            for i, character in enumerate(string):
                for word, value in SPELLED_OUT_NUMBERS.items():
                    if string[i:].startswith(word):
                        string = string.replace(word, str(value), 1)
            print(string, end="")
            
        numbers = [int(i) for i in re.findall(r'\d+', string)]
        print(numbers)
        
        first = [int(digit) for digit in str(numbers[0])][0]
        last = [int(digit) for digit in str(numbers[-1])][-1]
        
        return f"{first}{last}"
    
    def day1part1(self):
        output = 0
        
        with open(self.FILE_PATH, 'r') as file:
            for line in file:
                output += int(self.get_first_last_digits(line))
                
        return output
    
    def day1part2(self):
        output = 0
        
        with open(self.FILE_PATH, 'r') as file:
            for line in file:
                output += int(self.get_first_last_digits(line, True))
                
        return output

if __name__ == "__main__":
    day1 = Day1()
    output1 = day1.day1part1()
    day1 = Day1()
    output2 = day1.day1part2()
            
    print(f"Your output1 Sire:\n{output1}")
    print(f"Your output2 Sire:\n{output2}")