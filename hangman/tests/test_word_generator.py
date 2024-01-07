import os
import sys
import unittest

sys.path.insert(0, os.getcwd())

from game.word_generator import get_random_word


class TestWordGenerator(unittest.TestCase):
    def test_get_random_word_is_random(self):
        """
        Test case to verify that the get_random_word() function returns random words.

        It generates a list of random words by calling get_random_word() multiple times,
        and then checks if there are more than one unique word in the list.
        If there is only one unique word, it indicates that the function is not returning
        random words.

        This test assumes that the file_path variable points to a valid file containing
        a list of words.

        Raises:
            AssertionError: If the get_random_word() function does not appear to be random.
        """
        file_path = "resources/words.txt"
        random_words = [get_random_word(file_path)[0] for _ in range(100)]
        unique_words = set(random_words)
        self.assertGreater(
            len(unique_words), 1, "get_random_word() does not appear to be random"
        )

    def test_get_random_word_file_not_found(self):
        """
        Test case to verify that a FileNotFoundError is raised when the file is not found.
        """
        non_existent_file_path = "resources/non_existent_file.txt"
        with self.assertRaises(FileNotFoundError):
            get_random_word(non_existent_file_path)


if __name__ == "__main__":
    unittest.main()
