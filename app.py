'''
Author: Joe Braley
Last Modfied: 11/3/2021
Purpose: Parse text to detemine the top 100 most frequent words found
in the text. Users can input the data via command line file paths. Or,
if they prefer they can enter in the text via std input. If the user
uses file paths as inputs the files are opened and read line by line.
The program uses regex to strip punctuation from the line and transform
the input to lowercase. After each iteration we update a frequency map.
This map contains data relating to frequencies of three letter words found.
A similar process is followed when reading in user input from std in.
'''

from argparse import ArgumentParser
from typing import List

import fileinput
import re

class FrequentWordParser:
    ''' Frequent word parser class '''

    def __init__(self, word_count=100):
        self.frequency_map = {}
        self.word_count = word_count

    def fill_frequency_map(self, current_line: List):
        '''
            Args:
                current_line (list): list of lines to concatenate into
                    three letter sequences
            Returns:
                None
            Raises:
                None
        '''

        # iterate through the current line of data
        while len(current_line) > 2:
            # get the three word combod
            three_word_combo = " ".join([current_line[0], current_line[1], current_line[2]])

            # If we have seen this guy before then increment the count
            if three_word_combo in self.frequency_map:
                self.frequency_map[three_word_combo] += 1
            # else then add a new count
            else:
                self.frequency_map[three_word_combo] = 1
            # remove the first added element
            current_line.pop(0)

    def process_line_by_line_file(self, files: List):
        '''
            Will open each file supplied line by line. Clean the lines
                using helper functions. Update a master data store
                the print the frequencies out once all files have been read.
            Args:
                files (List): files to be opened and read line
                    by line
            Returns:
                None
            Raises:
                None
        '''

        # for each file supplied via command line
        for file in files:
            filled_array = []

            try:
                # open the file and read the file line by line
                # enforce encoding to be UTF-8
                with open(file, "r", encoding="utf-8") as file_in:
                    # get the current file line
                    file_lines = file_in.readline()

                    while file_lines:
                        self.clean_data(file_lines, filled_array)
                        self.fill_frequency_map(filled_array)
                        file_lines = file_in.readline()

            except FileNotFoundError:
                print(f"File not found! Please check the file path and try again.")

        # after reading in the file data print to the console
        self.print_frequency_map()

    def process_std_in(self, data: List):
        '''
            Calls helper function to process each line of standard in.

            Args:
                data: List of strings to process
            Returns:
                None
            Raises:
                None
        '''

        self.process_line_by_line_std_in(data)

    def process_line_by_line_std_in(self, data):
        '''
            For each line supplied via standard in we will clean the line.
            then fill the master data store with the frequencies of the cleaned
            data.

            Args:
                data (list): Text based data to be processed
            Returns:
                None
            Raises:
                None
        '''

        filtered_data = []

        for datum in data:
            self.clean_data(datum, filtered_data)
            self.fill_frequency_map(filtered_data)

        self.print_frequency_map()

    def print_frequency_map(self):
        '''
            Sorts the frequencies by the values in the hash map/dict in reverse
            order. While our current count is less than the allowed words to print
            output to the console/terminal.

            Args:
                None
            Returns:
                None
            Raises:
                None
        '''

        sorted_vals = dict(sorted(self.frequency_map.items(), key=lambda x : x[1], reverse=True))

        count = 0
        width = 30
        sorted_keys = list(sorted_vals.keys())

        print(f"============================ Top {self.word_count}: most frequent words found =======================")

        while count < self.word_count:
            print(f"{sorted_keys[count]:>{width}}          ------->                {sorted_vals[sorted_keys[count]]}")
            count += 1

        print(f"=================================== End ============================================")

    def open_file(self, files: List):
        '''
            Calls the function to open each file in the list one by one.
            Args:
                files (list) : list of files to open and process
            Returns:
                None
            Raises:
                None
        '''
        self.process_line_by_line_file(files)

    def clean_data(self, data, filled_array):
        '''
            Cleans the line supplied. Uses regex to remove punctutation and to find all the words
            in the line. Which returns as a list we can then turn each word to lowercase and
            add to the master data store filled_array.

            Args:
                data (string): line of text to clean and format
                filled_array (list): Data store which contains cleaned
                     and formatted lines of text
            Returns:
                None
            Raises:
                None
        '''

        stripped_data = re.sub("[^\w\s]", "", data.lower())
        parsed_data = re.compile("\\w+").findall(stripped_data)

        for datum in parsed_data:
            filled_array.append(datum.lower())


def main(data: List, files: List):
    '''
        Calls the proper entry point in the instance.

        Args:
            data (list): List containing the input lines read
                from standard in
            files (list): List of files to process
        Returns:
            None
        Raises:
            None
    '''

    parser = FrequentWordParser()

    if files:
        parser.open_file(files)

    elif data:
        parser.process_std_in(data)

    else:
        print(f"No data provided! Aborting.")

if __name__ == "__main__":

    parser = ArgumentParser()
    std_input = []

    def lower_line(line):
        '''
            Lowers each line supplied from standard in.

            Args:
                line (string): Line to clean
            Returns:
                lowered_line (list): List of strings which have been lowered
            Raises:
                None
        '''

        lowered_line = []

        for item in line:
            lowered_line.append(''.join(item.lower()))

        return lowered_line

    # add the arg parser
    parser.add_argument(
        'files',
        nargs="*",
        type=str,
        help="String file paths required to run parser."
    )

    # Parse the args
    args = parser.parse_args()

    # If no files supplied via args check standard in
    if not args.files:
        for line in fileinput.input(openhook=fileinput.hook_encoded("utf-8")):
            std_input.append(line)

    main(std_input, files=args.files)
