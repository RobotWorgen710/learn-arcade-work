import re

# This function takes in a line of text and returns
# a list of words in the line.


def split_line(line):
    return re.findall('[A-Za-z]+(?:\'[A-Za-z]+)?',line)


def main():
    """ Read in the file"""

    # Open the file
    my_file = open("dictionary.txt")

    # Create an empty list to hold the lines
    dictionary_list = []

    # Loop through each line of the file to correct the spacing
    for line in my_file:
        # Remove all the lines in between
        line = line.strip()

        # Add the items back into the list
        dictionary_list.append(line)

    # Close the file so it doesn't bog down the system
    my_file.close()

    # --- Linear search ---
    """ Doing a linear search for misspelled words """
    print("--- Linear Search ---")

    # Open the file
    alice = open("AliceInWonderLand200.txt")
    line_number = 0

    # Split the line in individual words
    for line in alice:
        word_list = split_line(line)

        line_number += 1

        for word in word_list:
            """ Searching the line """

            key = word.upper()

            current_list_position = 0

            while current_list_position < len(dictionary_list) and dictionary_list[current_list_position] != key:

                current_list_position += 1

                if current_list_position == len(dictionary_list):
                    print("Line: " + str(line_number) + " Possible misspelled word: " + word)

    alice.close()

    # --- Binary Search
    print("--- Binary Search ---")

    # Reopen file
    my_file = open("dictionary.txt")
    for line in my_file:
        # Remove all the lines in between
        line = line.strip()

        # Add the items back into the list
        dictionary_list.append(line)

        # Close the file so it doesn't bog down the system
    my_file.close()

    alice = open("AliceInWonderLand200.txt")
    line_number_binary = 0

    for line in alice:
        word_list = split_line(line)
        line_number_binary += 1

        for word in word_list:
            """ Searching the line """

            key = word.upper()
            lower_bound = 0
            upper_bound = len(dictionary_list) - 1
            found = False

            while lower_bound <= upper_bound and not found:

                # Find the middle position
                middle_pos = (lower_bound + upper_bound) // 2

                if dictionary_list[middle_pos] < key:
                    lower_bound = middle_pos + 1
                elif dictionary_list[middle_pos] > key:
                    upper_bound = middle_pos - 1
                else:
                    found = True

            if not found:
                print("Line: " + str(line_number_binary) + " Possible misspelled word: " + word)




if __name__ == '__main__':
    main()
