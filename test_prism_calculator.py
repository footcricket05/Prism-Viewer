import unittest
from prism_calculator import PrismCalculator

class TestPrismCalculator(unittest.TestCase):
    
    def test_surface_area(self):
        length, width, height = 3.0, 4.0, 5.0
        expected_surface_area = 94.0
        result = PrismCalculator.surface_area(length, width, height)
        self.assertEqual(result, expected_surface_area, "Surface area calculation is incorrect.")
    
    def test_volume(self):
        length, width, height = 3.0, 4.0, 5.0
        expected_volume = 60.0  
        result = PrismCalculator.volume(length, width, height)
        self.assertEqual(result, expected_volume, "Volume calculation is incorrect.")
    
if __name__ == '__main__':
    unittest.main()
