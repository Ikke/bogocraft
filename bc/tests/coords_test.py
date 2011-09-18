import unittest
from bc.utils.coords import tile_coords as tc

class CoordsTest(unittest.TestCase):

    def test_horizontal_coords(self):
        test_values = {
            (0, 0): (0, 0),
            (1, 0): (16, 16),
            (2, 0): (32, 32),
            (-1, -1): (0, -32)
        }
        for argument, result in test_values.items():
            self.assertEqual(tc(argument[0], argument[1]), result)

    def test_vertical_coords(self):
        test_values = {
            (0, 1): (-16, 16),
            (0, 2): (-32, 32),
            (1, 1): (0, 32)
        }
        for argument, result in test_values.items():
            self.assertEqual(tc(argument[0], argument[1]), result)
