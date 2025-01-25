# Write your solution here:
class SuperHero:
    def __init__(self, name: str, superpowers: str):
        self.name = name
        self.superpowers = superpowers

    def __str__(self):
        return f'{self.name}, superpowers: {self.superpowers}'


# The exercise template contains the class definition for a SuperHero.

# Please define a class named SuperGroup which represents a group of superheroes. 
# The class should contain the following members:

# Protected attributes name (str), location (str) and members (list)
# A constructor which takes the name and location of the group as arguments, in that order
# Getter methods for the name and location attributes
# A method named add_member(hero: SuperHero) which adds a new member to the group
# A method named print_group which prints out information about the group and its members, 
# following the format specified below
# An example of the class in action:

class SuperGroup():

    def __init__(self, name, location):
        # super().__init__()
        self._name = name
        self._location = location
        self._members = []

    @property
    def name(self):
        return self._name
    
    @property
    def location(self):
        return self._location

    def add_member(self, member: SuperHero):
        self._members.append(member)

    def print_group(self):
        first_line = f'{self._name}, {self._location}\n'
        second_line = "Members:\n"
        members_lines = []
        for member in self._members:
            members_lines.append(f'{member.name}, superpowers: {member.superpowers}')
        print(first_line + second_line + "\n".join(members_lines))

    
if __name__ == "__main__":
    superperson = SuperHero("SuperPerson", "Superspeed, superstrength")
    invisible = SuperHero("Invisible Inca", "Invisibility")
    revengers = SuperGroup("Revengers", "Emerald City")

    revengers.add_member(superperson)
    revengers.add_member(invisible)
    revengers.print_group()