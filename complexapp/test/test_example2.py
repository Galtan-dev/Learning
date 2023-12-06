import unittest
from src.example import func1


class TestModuleFile1(unittest.TestCase):
    def SetUp(self):
        print("Setting test up...")

    def test_func1_values(self):
        self.assertEqual(func1(3, 5), 11)
        self.assertAlmostEqual(func1(1.11, 2.5), 4.72)
        self.assertNotAlmostEqual(func1(1.11, 2.55), 5)

    def test_func1_types(self):
        with self.assertRaises(TypeError):
            func1(3, "asdf")


if __name__ == "__main__":
    unittest.main()