# Text Adventure

class Room:
    def __init__(self, description, north, east, south, west, up, down):
        self.description = description
        self.north = north
        self.east = east
        self.south = south
        self.west = west
        self.up = up
        self.down = down


def main():
    current_room = 0
    room_list = []

    """Great Room"""
    room0 = Room("You are in the great room. There is a room to the north ", 1, None, None, None, None, None)
    room_list.append(room0)

    """Living Room"""
    room1 = Room("You are in the living room. There are rooms to the north, south, west, and you can go upstairs", 4,
                 None, 0, 2, 8, None)
    room_list.append(room1)

    """Court Yard"""
    room2 = Room("You are in the court yard. There are rooms to the north, east, and west", 5, 1, None, 3, None, None)
    room_list.append(room2)

    """Master Bedroom"""
    room3 = Room("You are in the bedroom. There are rooms to the north and east", 6, 2, None, None, None, None)
    room_list.append(room3)

    """Kitchen"""
    room4 = Room("You are in the kitchen. There are rooms to the south and west", None, None, 1, 5, None, None)
    room_list.append(room4)

    """Computer Room"""
    room5 = Room("You are in the computer room. There are rooms to the east and south", None, 4, 2, None, None, None)
    room_list.append(room5)

    """Master Bathroom"""
    room6 = Room("You are in the bathroom. There is a room to the south", None, None, 3, None, None, None)
    room_list.append(room6)

    """Storage Room"""
    room7 = Room("You are in the storage room. There are rooms to the north and west", 9, None, None, 8, None, None)
    room_list.append(room7)

    """Upper Living Room"""
    room8 = Room("You are in the upper living room. There are rooms to the north, east, and you can go back downstairs",
                 10, None, None, 7, None, 1)
    room_list.append(room8)

    """Additional Bedroom"""
    room9 = Room("You are in a bedroom. There are rooms to the south and west", None, None, 7, 10, None, None)
    room_list.append(room9)

    """Bathroom"""
    room10 = Room("You are in the bathroom. There are rooms to the east and south", None, 9, 8, None, None, None)
    room_list.append(room10)

    done = False

    while not done:
        print("")
        print(room_list[current_room].description)

        direction = input("Which direction do you want to go? ")
        direction = direction.lower()

        if direction == "n" or direction == "north":
            """If the player goes north"""
            next_room = room_list[current_room].north
            if next_room is None:
                print("You cannot go that way.")
                next_room = current_room
            else:
                current_room = next_room

        elif direction == "e" or direction == "east":
            """If the player goes east"""
            next_room = room_list[current_room].east
            if next_room is None:
                print("You cannot go that way.")
                next_room = current_room
            else:
                current_room = next_room

        elif direction == "s" or direction == "south":
            """If the player goes east"""
            next_room = room_list[current_room].south
            if next_room is None:
                print("You cannot go that way.")
                next_room = current_room
            else:
                current_room = next_room

        elif direction == "w" or direction == "west":
            """If the play goes west"""
            next_room = room_list[current_room].west
            if next_room is None:
                print("You cannot go that way.")
                next_room = current_room
            else:
                current_room = next_room

        elif direction == "q" or direction == "quit":
            print("")
            quit = input("Are you sure you want to quit? ")
            if quit.lower() == "y" or quit.lower() == "yes":
                done = True
                print("")
                print("Quitters never win")
            else:
                done = False

        elif direction == "up" or direction == "up stairs" or direction == "upstairs" or direction == "u":
            next_room = room_list[current_room].up
            if next_room is None:
                print("You cannot go that way.")
                next_room = current_room
            else:
                current_room = next_room

        elif direction == "down" or direction == "d" or direction == "downstairs" or direction == "down stairs":
            next_room = room_list[current_room].down
            if next_room is None:
                print("You cannot go that way.")
                next_room = current_room
            else:
                current_room = next_room

        else:
            print("")
            print("The game doesn't understand what you typed. Please use one letter or the full word.")


if __name__ == '__main__':
    main()

