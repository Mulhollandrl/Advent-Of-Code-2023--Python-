import unittest
from main2 import Day2

class TestDay1(unittest.TestCase):   
    def test_part1(self):
        day2 = Day2(file_path="./Day 2/data/test1_input.csv")
        result = 8
        self.assertEqual(result, day2.day2_part1())
        
    def test_part2(self):
        day2 = Day2(file_path="./Day 2/data/test1_input.csv")
        result = 2286
        self.assertEqual(result, day2.day2_part2())
        
if __name__ == "__main__":
    unittest.main()