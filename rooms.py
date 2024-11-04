room_descriptions = [
    [ "A", "B", "C", "D", "E" ],
    [ "F", "G", "H", "I", "J" ],
    [ "K", "L", "M", "N", "O" ],
    [ "P", "Q", "R", "S", "T" ],
    [ "U", "V", "W", "X", "Y" ]
]
position = (3, 3)
while (True):

    x,y = position
    description = room_descriptions[y][x]
    print(position, ":", description)

    print("What now?")
    command = input()

    if command == "north":
        print("You move north...")
        y = y - 1
    elif command == "south":
        print("You move south...")
        y = y + 1
    elif command == "east":
        print("You move east...")
        x = x + 1
    elif command == "west":
        print("You move west...")
        x = x - 1
    elif command == "quit":
        break
    else:
        print("I don't know what " + command + " means...")

    position = (x,y)