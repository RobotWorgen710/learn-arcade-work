import re

# This function takes in a line of text and returns
# a list of words in the line.


def split_line(line):
    return re.findall('[A-Za-z]+(?:\'[A-Za-z]+)?',line)


def read_file_dictionary():
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
def linear_search():
    """ Doing a linear search for misspelled words """

    # Open the file
    alice = open("AliceInWonderLand200.txt")

    # Split the line in individual words
    for line in alice:
        word_list = split_line(line)

        for word in word_list:
            """ Searching the line """

            key = word.upper()

            current_list_position = 0

            while current_list_position < len(word_list) and word != key:
                current_list_position += 1
            if current_list_position == len(word_list):
                print("Possible misspelled word: " + word)




def main():
    read_file_dictionary()
    linear_search()


if __name__ == '__main__':
    main()
