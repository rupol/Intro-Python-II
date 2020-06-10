from room import Room
from player import Player

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance", "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", "Dim light filters in from the south. Dusty passages run north and east."),

    'overlook': Room("Grand Overlook", "A steep cliff appears before you, falling into the darkness. Ahead to the north, a light flickers in the distance, but there is no way across the chasm."),

    'narrow':   Room("Narrow Passage", "The narrow passage bends here from west to north. The smell of gold permeates the air."),

    'treasure': Room("Treasure Chamber", "You've found the long-lost treasure chamber! Sadly, it has already been completely emptied by earlier adventurers. The only exit is to the south."),
}


# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

# for key, value in room.items():
#     print(value)


# Declare players
player = {
    'kinga': Player('Kinga D Castle', 'leader', room['overlook']),
    'moose': Player('Y AE Spruce Moose', 'driver', room['outside']),
    'arms': Player('Arms McDaniels', 'muscle', room['narrow']),
}

# print(player['kinga'])

#
# Main
#

# Make a new player object that is currently in the 'outside' room.
current_player = player['kinga']
current_player.current_room = room['outside']

# Write a loop that:
choice = 0
print('Type q to quit at any time')

while True:
    # Prints the current room name
    print(current_player.current_room.name)

    # Prints the current description (the textwrap module might be useful here).
    print(current_player.current_room.description)


    # Waits for user input and decides what to do.
    choice = input(f'Where do you want to go next? North (n), South (s), East (e) or West (w)?: ')

    # If the user enters a cardinal direction, attempt to move to the room there.
    # Print an error message if the movement isn't allowed.
    try:
        # If the user enters "q", quit the game.
        if (choice == 'q'):
            break
        if choice == 'n' and current_player.current_room.n_to:
            current_player.current_room = current_player.current_room.n_to
            print('You move north into the...')
        if choice == 's' and current_player.current_room.s_to:
            current_player.current_room = current_player.current_room.s_to
            print('You move south into the...')
        if choice == 'e' and current_player.current_room.e_to:
            current_player.current_room = current_player.current_room.e_to
            print('You move east into the...')
        if choice == 'w' and current_player.current_room.w_to:
            current_player.current_room = current_player.current_room.w_to
            print('You move west into the...')
    except AttributeError:
        print('Please enter a valid direction (n/s/e/w)')
