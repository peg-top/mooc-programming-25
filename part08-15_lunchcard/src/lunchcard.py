# Write your solution here:


class LunchCard:
    def __init__(self, balance: float):
        self.balance = balance

    def __str__(self):
        return f'The balance is {self.balance:.1f} euros'
    
    def deposit_money(self, money: int):

        if money >= 0:
            self.balance += money
        else:
            raise ValueError(" You cannot deposit an amount of money less than zero")

    def eat_lunch(self):
        if self.balance >= 2.6:
            self.balance -= 2.6

    def eat_special(self):
        if self.balance >= 4.6:
            self.balance -= 4.6


def main():
    peter = LunchCard(20)
    grace = LunchCard(30)

    peter.eat_special()
    grace.eat_lunch()

    print(f'Peter: {str(peter)}')
    print(f'Grace: {str(grace)}')

    peter.deposit_money(20)
    grace.eat_special()

    print(f'Peter: {str(peter)}')
    print(f'Grace: {str(grace)}')

    peter.eat_lunch()
    peter.eat_lunch()

    grace.deposit_money(50)


    print(f'Peter: {str(peter)}')
    print(f'Grace: {str(grace)}')


# card = LunchCard(10)
# card.deposit_money(-10)

main()