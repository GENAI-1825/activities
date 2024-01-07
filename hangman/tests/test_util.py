import os
import sys
import unittest

sys.path.insert(0, os.getcwd())

from game.util import masked_word


class TestUtil(unittest.TestCase):
    def test_masked_word(self):
        """
        Test case to verify that the masked_word() function returns a masked version of the given word.
        """
        word = "hello"
        expected_result = "*****"
        self.assertEqual(
            masked_word(word),
            expected_result,
            "masked_word() did not return the expected result",
        )


if __name__ == "__main__":
    unittest.main()
