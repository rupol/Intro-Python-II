# Write a class to hold player information, e.g. what room they are in
# currently.
class Player:
    # attributes: name, current_room
    def __init__(self, name, role, current_room=None, inventory = []):
        self.name = name
        self.role = role
        self.current_room = current_room
        self.inventory = inventory
    
    def __str__(self):
        return f'{self.name.upper()}, our {self.role}, is in the {self.current_room}'

    def __repr__(self):
        return f'self.name = {self.name}, self.role = {self.role}, self.current_room = {self.current_room}'

    # picks up an item and adds it to the player inventory
    def on_take(self, item):
        print(f'You have picked up the {item}')
        self.inventory.append(item)

    # drops an item and removes it from the player inventory
    def on_drop(self, item):
        print(f'You have dropped the {item}')
        self.inventory.remove(item)
    
    # prints a list of the items in the player's inventory
    def get_inventory(self):
        if len(self.inventory) > 0:
            output = (f'You have the following items in your inventory:')
            for item in self.inventory:
                output += f'\n {item}'
            print(output)
        else:
            print(f'You have no items in your inventory')
