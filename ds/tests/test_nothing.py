import random
import unittest

class TestNothing(unittest.TestCase):

    def test_something(self):
        self.assertEqual(random.randint(1,3), 1)
