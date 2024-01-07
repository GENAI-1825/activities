import os
import sys
import unittest

sys.path.insert(0, os.getcwd())

from io import StringIO
from game.display import get_hangman


class TestDisplay(unittest.TestCase):
    def setUp(self):
        self.output = StringIO()

    def tearDown(self):
        self.output.close()

    def test_draw_life_6(self):
        """
        Test case to verify the output of draw function when life is 6.
        """
        expected_output = """
        _______
        |     |
              |
              |
              |
              |
      ________|
      """
        actual = get_hangman(6)
        self.assertEqual(actual, expected_output)

    def test_draw_life_5(self):
        """
        Test case to verify the output of draw function when life is 5.
        """
        expected_output = """
      _______
      |     |
      O     |
            |
            |
            |
    ________|
    """
        actual = get_hangman(5)
        self.assertEqual(actual, expected_output)

    def test_draw_life_4(self):
        """
        Test case to verify the output of draw function when life is 4.
        """
        expected_output = """
      _______
      |     |
      O     |
      |     |
            |
            |
    ________|
    """
        actual = get_hangman(4)
        self.assertEqual(actual, expected_output)

    def test_draw_life_3(self):
        """
        Test case to verify the output of draw function when life is 3.
        """
        expected_output = """
      _______
      |     |
      O     |
     /|     |
            |
            |
    ________|
    """
        actual = get_hangman(3)
        self.assertEqual(actual, expected_output)

    def test_draw_life_2(self):
        """
        Test case to verify the output of draw function when life is 2.
        """
        expected_output = """
      _______
      |     |
      O     |
     /|\\    |
            |
            |
    ________|
    """
        actual = get_hangman(2)
        self.assertEqual(actual, expected_output)

    def test_draw_life_1(self):
        """
        Test case to verify the output of draw function when life is 1.
        """
        expected_output = """
      _______
      |     |
      O     |
     /|\\    |
     /      |
            |
    ________|
    """
        actual = get_hangman(1)
        self.assertEqual(actual, expected_output)

    def test_draw_life_0(self):
        """
        Test case to verify the output of draw function when life is 0.
        """
        expected_output = """
      _______
      |     |
      O     |
     /|\\    |
     / \\    |
            |
    ________|
    """
        actual = get_hangman(0)
        self.assertEqual(actual, expected_output)


if __name__ == "__main__":
    unittest.main()
