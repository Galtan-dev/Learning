import sys
sys.path.append("C:\\Users\\jakub\\PycharmProjects\\Learning\\complexapp")
sys.path.append("C:\\Users\\jakub\\PycharmProjects\\Learning\\complexapp\\src")
sys.path.append("C:\\Users\\jakub\\PycharmProjects\\Learning\\complexapp\\test")
import unittest
import test_example as tfm
import test_example2 as tfm2

# initialize test suite
loader = unittest.TestLoader()
suite = unittest.TestSuite()

# add test to the test suite
suite.addTests(loader.loadTestsFromModule(tfm))
suite.addTests(loader.loadTestsFromModule(tfm2))


runner = unittest.TextTestRunner(verbosity=3)
result = runner.run(suite)