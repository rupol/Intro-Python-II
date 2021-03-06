# Implement a class to hold room information. This should have name and
# description attributes.
class Room:
    # attributes: name, description
    def __init__(self, name, description, items = []):
        self.name = name
        self.description = description
        self.s_to = None
        self.e_to = None
        self.w_to = None
        self.n_to = None
        self.items = items

    def __str__(self):
        output = f'{self.name.upper()}\n{self.description}'

        if len(self.items) > 0:
            output  += "\nYou see the following items:"
            for item in self.items:
                output += f'\n {item.name} - {item.description}'
        return output

    def __repr__(self):
        return f'self.name = {self.name}, self.description = {self.description}'