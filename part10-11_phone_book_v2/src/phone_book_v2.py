
# Write your solution here:

class Person:

    def __init__(self, name):
        self.__name = name
        self.__numbers = []
        self.__address = None

    def __str__(self):
        return f'{self.__name} : {self.__numbers} : {self.__address}'

    # @property
    def name(self):
        return self.__name
    # @property
    def numbers(self):
        return self.__numbers
    
    # @property
    def address(self):
        return self.__address
    
    def add_number(self, number):
        self.__numbers.append(number)

    def add_address(self, address):
        self.__address = address


class PhoneBook:
    def __init__(self):
        self.__persons = {}

    def __str__(self):
        return f'{self.__persons}'

    def add_number(self, name: str, number: str):
        if not name in self.__persons:
            self.__persons[name] = Person(name)
        self.__persons[name].add_number(number)

    def get_entry(self, name: str):
        return self.__persons.get(name, None)

    def all_entries(self):
        return self.__persons
    
    def add_address(self, name, address):
        if not name in self.__persons:
            self.__persons[name] = Person(name)
        self.__persons[name].add_address(address)

class PhoneBookApplication:
    def __init__(self):
        self.__phonebook = PhoneBook()

    def help(self):
        print("commands: ")
        print("0 exit")
        print("1 add number")
        print("2 search")
        print("3 add address")

    def add_number(self):
        name = input("name: ")
        number = input("number: ")
        self.__phonebook.add_number(name, number)

    def search(self):
        name = input("name: ")
        person = self.__phonebook.get_entry(name)
        if not person:
            print("number unknown")
            print("address unknown1")
        else:
            if not person.numbers():
                print("number unknown") 
            else:
                for number in person.numbers():
                    print(number)
            if not person.address():
                print("address unknown1")
            else:
                print(person.address())

    def add_address(self):
        name = input("name: ")
        address = input("address: ")
        self.__phonebook.add_address(name, address)        

    def execute(self):
        self.help()
        while True:
            print("")
            command = input("command: ")
            if command == "0":
                break
            elif command == "1":
                self.add_number()
            elif command == "2":
                self.search()
            elif command == "3":
                self.add_address()
            else:
                self.help()



# when testing, no code should be outside application except the following:
application = PhoneBookApplication()
application.execute()


# person = Person("Eric")
# print(person.name())
# print(person.numbers())
# print(person.address())
# person.add_number("040-123456")
# person.add_address("Mannerheimintie 10 Helsinki")
# print(person.numbers())
# print(person.address())

# phonebook = PhoneBook()
# phonebook.add_number("Eric", "02-123456")
# print(phonebook.get_entry("Eric"))
# print(phonebook.get_entry("Emily"))

# print(phonebook)