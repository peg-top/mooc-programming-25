# DO NOT CHANGE THE CODE OF THE CLASS
# ShoppingList. Write yous solution under it!
class ShoppingList:
    def __init__(self):
        self.products = []

    def number_of_items(self):
        return len(self.products)

    def add(self, product: str, number: int):
        self.products.append((product, number))

    def item(self, n: int):
        return self.products[n - 1][0]

    def amount(self, n: int):
        return self.products[n - 1][1]

# -------------------------
# Write your solution here:
# -------------------------


def total_units(my_list: ShoppingList):
    return sum([x[1] for x in my_list.products])

if __name__ == "__main__":

    my_list = ShoppingList()
    my_list.add("bananas", 10)
    my_list.add("apples", 5)
    my_list.add("pineapple", 1)

    print(total_units(my_list))


    # print(shopping_list.number_of_items())
    # print(shopping_list.item(1))
    # print(shopping_list.amount(1))
    # print(shopping_list.item(2))
    # print(shopping_list.amount(2))