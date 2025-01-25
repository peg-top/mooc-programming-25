# Write your solution here:

class Item:
    def __init__(self, name, weight):
        self._name = name
        self._weight = weight

    def name(self):
        return self._name

    def weight(self):
        return self._weight

    def __str__(self):
        return f"{self._name} ({self._weight} kg)"

class Suitcase:
    def __init__(self, max_weight):
        self.max_weight = max_weight
        self.items = []

    def add_item(self, item):
        if self.weight() + item.weight() <= self.max_weight:
            self.items.append(item)

    def weight(self):
        return sum(item.weight() for item in self.items)

    def print_items(self):
        for item in self.items:
            print(item)

    def heaviest_item(self):
        if not self.items:
            return None
        return max(self.items, key=lambda item: item.weight())

    def __str__(self):
        item_count = len(self.items)
        item_word = "item" if item_count == 1 else "items"
        return f"{item_count} {item_word} ({self.weight()} kg)"

class CargoHold:
    def __init__(self, max_weight):
        self.max_weight = max_weight
        self.suitcases = []

    def add_suitcase(self, suitcase):
        if self.weight() + suitcase.weight() <= self.max_weight:
            self.suitcases.append(suitcase)

    def weight(self):
        return sum(suitcase.weight() for suitcase in self.suitcases)

    def print_items(self):
        for suitcase in self.suitcases:
            suitcase.print_items()

    def __str__(self):
        suitcase_count = len(self.suitcases)
        suitcase_word = "suitcase" if suitcase_count == 1 else "suitcases"
        return f"{suitcase_count} {suitcase_word}, space for {self.max_weight - self.weight()} kg"
            
        

if __name__ == "__main__":

    book = Item("ABC Book", 2)
    phone = Item("Nokia 3210", 1)
    brick = Item("Brick", 4)

    suitcase = Suitcase(5)
    print(suitcase)

    suitcase.add_item(book)
    print(suitcase)

    suitcase.add_item(phone)
    print(suitcase)

    suitcase.add_item(brick)
    print(suitcase)