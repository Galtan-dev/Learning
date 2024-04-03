import unittest
from physical_units_utils import convert_length as length
from physical_units_utils import convert_speed as speed
from physical_units_utils import convert_temperature as temperature


class test_speed(unittest.TestCase):
    def test_speed_values(self):
        self.assertAlmostEqual(speed(100, "kph", "mph"), 160.934)
        self.assertNotAlmostEqual(speed(100, "kph", "mph"), 54.35)

    def test_speed_types(self):
        with self.assertRaises(ValueError):
            speed("str", "mph", "kph")

class test_temperature(unittest.TestCase):
    def test_temperature_values(self):
        self.assertAlmostEqual(temperature(100, "K", "F"), 310.92777777777775)
        self.assertNotAlmostEqual(temperature(100, "K", "F"), 308.654)

    def test_temperature_types(self):
        with self.assertRaises(ValueError):
            temperature("str", "F", "K")

class test_length(unittest.TestCase):
    def test_length_values(self):
        self.assertEqual(length(1000, "m", "km"), 1)
        self.assertNotEqual(length(1000, "m", "km"), 15)

    def test_length_types(self):
        with self.assertRaises(ValueError):
            length("str", "m", "km")

if __name__ == "__main__":
    unittest.main()