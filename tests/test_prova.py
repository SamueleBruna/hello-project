import unittest

from hello_project.hello_world import hello_world
from unittest.mock import patch


class MyTestCase(unittest.TestCase):

    # mocking the print function that is called by hello_world
    @patch('builtins.print')
    def test_hello_world_1(self, mock_print):
        # The actual test
        name = 'Samu'
        hello_world(name)
        # asserting that the print function is called passing the string 'Hello World!'
        mock_print.assert_called_with(f'Hello World {name}!')


if __name__ == '__main__':
    unittest.main()
