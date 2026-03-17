import unittest
from lecture import randomised_function
from unittest.mock import patch

class MyTestCase(unittest.TestCase):

    @patch('random.randint')
    @patch('lecture.is_small')
    def test_randomised_function_mock1(self, mock_randint, mock_is_small):
        mock_randint.return_value = 3
        mock_is_small.return_value = True 
        self.assertEqual('software', randomised_function())  # This will pass or fail randomly
        # TODO: Can we make this test deterministic? (HINT: Mock testing)

    @patch('random.randint')
    def test_randomised_function_mock2(self, mock_randint):
        mock_randint.return_value = 6
        self.assertEqual('engineering', randomised_function())  # This will pass or fail randomly
        # TODO: Can we make this test deterministic? (HINT: Mock testing)