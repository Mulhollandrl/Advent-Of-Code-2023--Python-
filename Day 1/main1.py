import re
from enums import SPELLED_OUT_NUMBERS

class Day1:
    def __init__(self, file_path = "data/day1part1_input.csv") -> None:
        self.FILE_PATH = file_path
                
    def get_first_last_digits(self, string, spelled=False):
        if spelled:
            for word, num in SPELLED_OUT_NUMBERS.items():
                string = string.replace(word, str(num))
            
        numbers = [int(i) for i in re.findall(r'\d+', string)]
        
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
                print(self.get_first_last_digits(line, True))
                output += int(self.get_first_last_digits(line, True))
                
        return output

if __name__ == "__main__":
    day1 = Day1()
    output = day1.day1part1()
            
    print(f"Your output Sire:\n{output}")