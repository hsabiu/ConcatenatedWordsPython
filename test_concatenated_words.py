# -----------------------------------------------------------------------------
# Author: Habib Sabiu
# Date: 16 August, 2018
#
# Purpose: Unit test module for the WordsConcatenated class
# -----------------------------------------------------------------------------


import unittest
from concatenated_words import WordsConcatenated


class TestWordsConcatenated(unittest.TestCase):

    def test_read_data(self):
        """Verify that reading data from a file that does not exist raise an Exception
        and terminated the program"""

        with self.assertRaises(Exception):
            WordsConcatenated().read_data('/dummy_file.txt')

    def test_write_output(self):
        """Verify that the errors returned when writing the result to the output file are handled"""

        all_words = WordsConcatenated().read_data('dictionary.txt')
        six_letter_words = WordsConcatenated().get_six_letter_words(all_words)
        concatenated_words = WordsConcatenated().get_concatenated_words(six_letter_words, all_words)

        with self.assertRaises(Exception):
            WordsConcatenated().write_output(concatenated_words, "/dummy/path/")

    def test_get_six_letter_words(self):
        """Verify that all the words returned by the get_six_letter_words method have
        exactly 6 letters"""

        all_words = WordsConcatenated().read_data('dictionary.txt')
        six_letter_words = WordsConcatenated().get_six_letter_words(all_words)
        for word in six_letter_words:
            self.assertEqual(len(word), 6)

    def test_get_concatenated_words(self):
        """Verify that all the words returned by the get_concatenated_words method are built
        from two concatenated smaller words that exist in the giving dictionary of words"""

        all_words = WordsConcatenated().read_data('dictionary.txt')
        six_letter_words = WordsConcatenated().get_six_letter_words(all_words)
        concatenated_words = WordsConcatenated().get_concatenated_words(six_letter_words, all_words)

        for word in concatenated_words:
            smaller_words, concatenated = word.split("=>")
            smaller_words = smaller_words.split("+")
            word_1 = smaller_words[0]
            word_2 = smaller_words[1]

            self.assertTrue(word_1.strip() in all_words)
            self.assertTrue(word_2.strip() in all_words)
            self.assertTrue(concatenated.strip() in all_words)


if __name__ == '__main__':
    unittest.main()
