# -----------------------------------------------------------------------------
# Author: Habib Sabiu
# Date: 16 August, 2018
#
# Purpose: A python module to find all six-letter words that are built from
#          two concatenated smaller words from a given dictionary of words
#
#  Usage: python concatenated_words.py input_file output_file
#
# Example usage: python concatenated_words.py dictionary.txt output.txt
# -----------------------------------------------------------------------------

import sys
import datetime


class WordsConcatenated:

    @staticmethod
    def read_data(input_path):
        """Helper method to read data from a text file into a 'set' data structure

        Args:
            input_path: Relative or absolute path to the input text file containing dictionary of words

        Returns:
            This method returns a 'set'. Each element of the set represents a single
            line from the input text file.

        Note:
            The time complexity of this method is O(n) in the worse case, where n
            is the number of lines in the input file
        """

        try:
            # I use 'set' data structure to provide fast membership testing
            words_read = set()
            with open(input_path) as input_file:
                for line in input_file:
                    words_read.add(line.strip())
            return words_read
        except Exception as err:
            raise Exception

    @staticmethod
    def write_output(words_list, output_file):
        """Helper method to write data from a 'list' data structure to an output text file

        Args:
            output_file: Relative or absolute path to the output file
            words_list: A 'list' containing words of exactly six character length that are built
                        of two concatenated smaller words

        Note:
            This method does not return anything. It simply writes the data of the 'words_list'
            into a text 'output_file', with each line of the output file containing a single word.
            If the 'output_file' does not exist, the method would create the file and write to it.
            If the file already exist, the method would first truncate the file before writing to it.

        """

        try:
            with open(output_file, "w") as output:
                output.write("\n".join(words_list))
        except Exception as err:
            raise Exception

    @staticmethod
    def get_six_letter_words(words_all):
        """A method that return all words of exactly six characters long from a 'set' of
           a given dictionary of words

        Args:
            words_all: A 'set' containing all the words from a given dictionary of words

        Returns:
            This method return a 'set' containing words of exactly six character long

        Note:
            The time complexity of this method is O(n) in the worse case, where n
            is the number of elements in the 'words_all' set
        """

        return {word for word in words_all if len(word) == 6}

    @staticmethod
    def get_concatenated_words(words_six_letters, words_all):
        """A method that find and return all six-letter words that are built of two
           concatenated smaller words from a given dictionary of words

        Args:
            words_six_letters:  A 'set' containing all the words of exactly six character long
            words_all: A 'set' containing all the words from a given dictionary of words

        Returns:
            This method returns a 'list' containing words of exactly six character length
            that are built of two concatenated smaller words from 'words_all' set

        Note:
            Each element of the output list is a string in the following format:
                word_1 + word_2 => concatenated_word

            For example, if the word is 'indoor', the method would add the following string to the list:
                in + door => indoor

            The time complexity of this method is O(n) + (5 * O(m)) in the worse case, where n is the
            number of elements in the 'words_six_letters' set and m is the number of elements in the 'words_all' set

            Since the running time of the method would be dominated by the size of 'words_all' set as the
            number of words in the input dictionary gets larger, the worse case time complexity of this
            method is O(m), where m is size of the input dictionary of words.
        """

        concatenated = []

        # Loop through all the words provided in the 'words_six_letter' set. For each word, try
        # to form a smaller word by extracting the letters of the word from the beginning to the
        # current loop iteration index. If the smaller word formed exist in the given dictionary
        # and the remaining letters of the word form a smaller word that also exist in the dictionary,
        # add the word to the list of six-letter words that are built of two concatenated smaller words
        for word in words_six_letters:
            for i in range(1, len(word) + 1):
                if word[0:i] in words_all and word[i:] in words_all:
                    temp_str = word[0:i] + " + " + word[i:] + " => " + word
                    concatenated.append(temp_str)

        return concatenated


if __name__ == "__main__":
    # Get the input and output file form command line arguments
    input_file_path = sys.argv[1]
    output_file_path = sys.argv[2]

    start_time = datetime.datetime.now()

    # Read the dictionary words into a 'set'
    all_words = WordsConcatenated().read_data(input_file_path)

    # Get only the words with exactly six letters
    six_letter_words = WordsConcatenated().get_six_letter_words(all_words)

    # Get only the words that are built of two concatenated smaller words
    concatenated_words = WordsConcatenated().get_concatenated_words(six_letter_words, all_words)

    # Write the output of the concatenated words to an output file
    WordsConcatenated().write_output(concatenated_words, output_file_path)

    end_time = (datetime.datetime.now() - start_time).total_seconds() * 1000

    print("---------------------------------------------")
    print("SUCCESS: Application execution time = {} ms".format(round(end_time)))
    print("---------------------------------------------")
