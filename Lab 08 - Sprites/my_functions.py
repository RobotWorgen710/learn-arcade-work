
def foo():
    print("Foo!")


def read_in_file(filename):
    # --- Read in a file, and put in a list
    name_list = []

    # Open a file for reading
    my_file = open(filename)

    for line in my_file:
        line = line.strip()
        name_list.append(line)

    my_file.close()

    return name_list