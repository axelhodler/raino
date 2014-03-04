import unittest
import main

class TestMain(unittest.TestCase):
    def test_print(self):
        self.assertEqual(3, main.main())
