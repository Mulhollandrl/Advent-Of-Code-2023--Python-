import unittest
from main1 import Day1

class TestDay1(unittest.TestCase):   
    def test_part1(self):
        day1 = Day1(file_path="./Day 1/data/test1_input.csv")
        result = 142
        self.assertEqual(result, day1.day1part1())
        
    def test_part2(self):
        day1 = Day1(file_path="./Day 1/data/test2_input.csv")
        result = 281
        self.assertEqual(result, day1.day1part2())
        
if __name__ == "__main__":
    unittest.main()