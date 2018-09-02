# Introduction:
This project consist of a python module (concatenated_words.py) and a unit test (concatenated_words.py) module. The concatenated_words.py implements a logic for finding all six-letter words that are built from two concatenated smaller words from a given dictionary of words (dictionary.txt).

## Running the python module:
To run the python module, execute the following command in the project root directory:

    python concatenated_words.py dictionary.txt output.txt

On successful execution, the application would generate a text file (output.txt) containing the results

## Running the unit tests:
I have included unit tests containing four test cases to verify the correctness of the solution. To run the unit tests, execute the following commands from the project root directory:

    python -m unittest test_concatenated_words.py

## Test cases implemented:
- Test case 1: This test case verify that reading data from a file that does not exist raised an Exception and terminated the program

- Test case 2: This test case verify that all the words returned by the "get_six_letter_words" method have exactly 6 letters by looping through all the returned words and checking their length

- Test case 3: This test case verify that all the words returned by the "get_concatenated_words" method are built from two concatenated smaller words that exist in the giving dictionary of words. The test method loop through all the returned words and check that both the two smaller words and the concatenated word exist in the input dictionary.

- Test case 4: This test case verify that errors returned when writing the result to the output file are handled