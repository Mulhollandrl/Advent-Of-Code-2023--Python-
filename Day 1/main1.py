from enums import SPELLED_OUT_NUMBERS

class Day1:
    def __init__(self, file_path = "./Day 1/data/day1part1_input.csv") -> None:
        self.FILE_PATH = file_path
                
    def get_first_last_digits(self, string, spelled=False):
        numbers = []
        
        for i, char in enumerate(string):
            if char.isdigit():
                numbers.append(char)
            
            if spelled:
                for word, value in SPELLED_OUT_NUMBERS.items():
                    if string[i:].startswith(word):
                        numbers.append(value)
        
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
    output2 = day1.day1part2()
            
    print(f"Your output1 Sire:\n{output1}")
    print(f"Your output2 Sire:\n{output2}")