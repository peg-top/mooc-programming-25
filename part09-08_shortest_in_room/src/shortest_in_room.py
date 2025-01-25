# WRITE YOUR SOLUTION HERE:
class Person:
    def __init__(self, name: str, height: int):
        self.name = name
        self.height = height

    def __str__(self):
        return self.name
class Room:
    def __init__(self, persons = None):
        self.persons = persons if persons is not None else []

    def add(self, person):
        self.persons += [person]

    def is_empty(self):
        return len(self.persons) == 0

    def print_contents(self):
        print(f'There are {len(self.persons)} persons in the room, and their combined height is {sum([person.height for person in self.persons])} cm')
        print("\n".join([f'{person.name} ({person.height} cm)' for person in sorted(self.persons, key=lambda x: x.height, reverse=True)]))

    def shortest(self):
        if not self.persons:
            return None
        return min(self.persons, key=lambda x: x.height)

    def remove_shortest(self):

        shortest = self.shortest()

        if shortest:
            self.persons.remove(shortest)
            return shortest
        
        return None
    
if __name__ == "__main__":

    # room = Room()
    # print("Is the room empty?", room.is_empty())
    # room.add(Person("Lea", 183))
    # room.add(Person("Kenya", 172))
    # room.add(Person("Ally", 166))
    # room.add(Person("Nina", 162))
    # room.add(Person("Dorothy", 155))
    # print("Is the room empty?", room.is_empty())
    # room.print_contents()

    room = Room()

    room.add(Person("Lea", 183))
    room.add(Person("Kenya", 172))
    room.add(Person("Nina", 162))
    room.add(Person("Ally", 166))
    room.print_contents()

    print()

    removed = room.remove_shortest()
    print(removed)
    print(f"Removed from room: {removed.name}")

    print()

    room.print_contents()