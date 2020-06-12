from room import Room
from player import Player
from item import Item

# Declare all items
sword = Item('sword', 'fit for a queen')
cup = Item('cup', 'golden, has a little black hole in it')
blood = Item('blood', 'warm, feels good')

# Declare all the rooms
room = {
    'outside':  Room("Outside Cave Entrance", "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", "Dim light filters in from the south. Dusty passages run north and east.", [blood]),

    'overlook': Room("Grand Overlook", "A steep cliff appears before you, falling into the darkness. Ahead to the north, a light flickers in the distance, but there is no way across the chasm."),

    'narrow':   Room("Narrow Passage", "The narrow passage bends here from west to north. The smell of gold permeates the air."),

    'treasure': Room("Treasure Chamber", "You've found the long-lost treasure chamber! Sadly, it has already been completely emptied by earlier adventurers. The only exit is to the south.", [sword, cup]),
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

# print(room['foyer'])

# Declare players
player = {
    1: Player('Kinga D Castle', 'leader', room['foyer']),
    2: Player('Y AE Spruce Moose', 'driver', room['outside']),
    3: Player('Arms McDaniels', 'muscle', room['narrow']),
}

# print(player['kinga'])

#
# Main
#
ready_player = True # should be False to start
thematic_break = r"/////\\\\\\/////\\\\\\/////\\\\\\/////\\\\\\/////\\\\\\/////\\\\\\\//////\\\\\\"

# intro text
print(thematic_break)
print('//////////////////////////////// BOY_PROBLEMS ////////////////////////////////')
print('                A Carly Rae Jepsen-themed heist text adventure                ')
print(thematic_break)
print('                          Type q to quit at any time                          ')

current_player = player[1]
"""
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
        player_choice = int(player_choice)
        if player_choice >= 0 and player_choice < len(player.items()):
            current_player = player[player_choice]
            print(f'You have chosen {current_player.name}')
            ready_player = True
        else:
            print(thematic_break)
            print('Player does not exist. Please choose a valid player #.')
            print(thematic_break)

    except ValueError:
        print(thematic_break)
        print("Please enter a valid number")
        print(thematic_break)
"""

# Write a loop that:
choice = 0

while ready_player == True:
    print(thematic_break)
    # Prints the current room name, description, and any items (the textwrap module might be useful here).
    print(current_player.current_room)

    # Waits for user input and decides what to do.
    # print(current_player.current_room)
    direction_options = True
    choice = input(f'What do you want to do? You can move n, s, e, or w OR take, or drop an item: ').split()
    if len(choice) == 1:
        choice = choice[0]
        # If the user enters "q", quit the game
        if (choice == 'q'):
            break
        # If the user enters a cardinal direction, attempt to move to the room there
        elif choice in {'n', 's', 'e', 'w'}:
            if getattr(current_player.current_room, f'{choice}_to') is not None:
                current_player.current_room = getattr(current_player.current_room, f'{choice}_to')
                print('You move to the ...')
            # Print an error message if the movement isn't allowed
            else:
                print(thematic_break)
                print('You can\'t move in that direction. Please try again.')
        elif (choice == 'i' or choice == 'inventory'):
            current_player.get_inventory()
        # Print an error message if the input isn't a valid direction
        else:
            print(thematic_break)
            print('Please enter a valid direction (n/s/e/w)')
    elif len(choice) == 2:
        user_verb = choice[0]
        user_item = choice[1]
        if (user_verb == 'take' or user_verb == 'get'):
            if len(current_player.current_room.items) > 0:
                for item in current_player.current_room.items:
                    print(item)
                    if item.name == user_item:
                        current_player.on_take(user_item)
                        current_player.current_room.items.remove(item)
                    else:
                        print(f'Sorry, that item doesn\'t exist in the current room')
            else:
                print(f'Sorry, there are no items in the current room')
        elif (user_verb == "drop"):
            current_player.on_drop(user_item)
