from enums import MAXIMUMS

class Day2:
    def __init__(self, file_path="./Day 2/data/puzzle_input.csv") -> None:
        self.FILE_PATH = file_path
        
    def is_possible(self, line):
        games = line.strip("\n").split("; ")
        
        for game in games:
            cubes = game.split(", ")
            
            for cube in cubes:
                number, color = cube.split(" ")
                
                if int(number) > MAXIMUMS[color]:
                    return False
                
        return True
    
    def get_min_power_cubes(self, line):
        games = line.strip("\n").split("; ")
        minimums = {
            "red": 0,
            "green": 0,
            "blue": 0
        }
        
        for game in games:
            cubes = game.split(", ")
            
            for cube in cubes:
                number, color = cube.split(" ")
                
                if int(number) > minimums[color]:
                    minimums[color] = int(number)
                    
        return minimums["red"] * minimums["green"] * minimums["blue"]
    
    def day2_part1(self):
        output = 0
        
        with open(self.FILE_PATH, 'r') as file:
            for line in file:
                title, game = line.split(": ")
                
                if self.is_possible(game):
                    output += int(title.split(" ")[1])
                
        return output
    
    def day2_part2(self):
        output = 0
        
        with open(self.FILE_PATH, 'r') as file:
            for line in file:
                title, game = line.split(": ")
                
                output += self.get_min_power_cubes(game)
                
        return output
    
    
if __name__ == "__main__":
    day2 = Day2()
    output1 = day2.day2_part1()
    output2 = day2.day2_part2()
    
    print(f"Your output for part 1, Sire:\n{output1}")
    print(f"Your output for part 1, Sire:\n{output2}")