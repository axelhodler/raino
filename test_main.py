import unittest
import main
from mock import patch

class TestMain(unittest.TestCase):
    def test_print(self):
        obj = main.Main()

        with patch('builtins.print') as mock:
            obj.print_sth()

        mock.assert_called_with('lol')
