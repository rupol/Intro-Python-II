# Write a class to hold player information, e.g. what room they are in
# currently.
class Player:
    # attributes: name, current_room
    def __init__(self, name, role, current_room):
        self.name = name
        self.role = role
        self.current_room = current_room
    
    def __str__(self):
        return f'{self.name}, our {self.role}, is in the {self.current_room}'

    def __repr__(self):
        return f'self.name = {self.name}, self.role = {self.role}, self.current_room = {self.current_room}'
