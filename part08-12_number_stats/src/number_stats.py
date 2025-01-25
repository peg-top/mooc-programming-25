# Write your solution here!
class  NumberStats:
    def __init__(self):
        self.numbers = []

    def add_number(self, number:int):
        if number > -1:
            self.numbers += [number]

    def count_numbers(self):
        return len(self.numbers)

    def get_sum(self):
        return sum(self.numbers)

    def average(self):
        try:
            return self.get_sum()/self.count_numbers()
        except:
            print("Error")

# if __name__ == "__main__":

# def main(): 
print("Please type in integer numbers:")
stats = NumberStats()
even = NumberStats()
odd = NumberStats()
while True:
    try:
        num = int(input())
    except:
        print("Input only integer")
    if num == -1:
        break
    if num % 2 == 0:
        even.add_number(num)
    else:
        odd.add_number(num)
    stats.add_number(num)
    
print(f'Sum of numbers: {stats.get_sum()}')
print(f'Mean of numbers: {stats.average()}')
print(f'Sum of even numbers: {even.get_sum()}')
print(f'Sum of odd numbers: {odd.get_sum()}')


# if __name__ == "__main__":
# main()


