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
ready_player = False
thematic_break = r"/////\\\\\\/////\\\\\\/////\\\\\\/////\\\\\\/////\\\\\\/////\\\\\\\//////\\\\\\"

# intro text
print(thematic_break)
print('//////////////////////////////// BOY_PROBLEMS ////////////////////////////////')
print('                A Carly Rae Jepsen-themed heist text adventure                ')
print(thematic_break)
print('                          Type q to quit at any time                          ')

# print all player options
i = 1
for key, value in player.items():
    print(f'{i}. {value.name}, the {value.role}')
    i += 1

print(thematic_break)
player_choice = -1

# player choice
while ready_player == False:
    # waits for player input
    player_choice = input('CHOOSE YOUR PLAYER (#): ')

    # assign the player input to be the current player
    try:
        if (player_choice == 'q'):
            break
        if int(player_choice) == 1:
            current_player = player['kinga']
            ready_player = True
        if int(player_choice) == 2:
            current_player = player['moose']
            ready_player = True
        if int(player_choice) == 3:
            current_player = player['arms']
            ready_player = True
        # add error handling for other options
        # else:
        #     print('Your selected player does not exist')
    except ValueError:
        print("Please enter a valid number")


# Write a loop that:
choice = 0

while ready_player == True:
    print(thematic_break)
    # Prints the current room name
    print(current_player.current_room.name)

    # Prints the current description (the textwrap module might be useful here).
    print(current_player.current_room.description)


    # Waits for user input and decides what to do.
    # print(current_player.current_room)
    direction_options = True
    choice = input(f'Where do you want to go next? North (n), South (s), East (e) or West (w)?: ')

    # If the user enters a cardinal direction, attempt to move to the room there.
    # Print an error message if the movement isn't allowed.
    try:
        # If the user enters "q", quit the game.
        if (choice == 'q'):
            break
        if choice == 'n' and current_player.current_room.n_to:
            current_player.current_room = current_player.current_room.n_to
            print(thematic_break)
            print('You move north into the...')
        if choice == 's' and current_player.current_room.s_to:
            current_player.current_room = current_player.current_room.s_to
            print(thematic_break)
            print('You move south into the...')
        if choice == 'e' and current_player.current_room.e_to:
            current_player.current_room = current_player.current_room.e_to
            print(thematic_break)
            print('You move east into the...')
        if choice == 'w' and current_player.current_room.w_to:
            current_player.current_room = current_player.current_room.w_to
            print(thematic_break)
            print('You move west into the...')
        # add error handling for other options
        # else:
        #     print(thematic_break)
        #     print('Please enter a valid direction (n/s/e/w)')
    except AttributeError:
        print(thematic_break)
        print('Please enter a valid direction (n/s/e/w)')
