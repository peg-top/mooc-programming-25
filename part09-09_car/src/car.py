# WRITE YOUR SOLUTION HERE:

class Car:

    def __init__(self):
        self.__odometer = 0
        self.__tank = 0

    def __str__(self):
        return f'Car: odometer reading {self.__odometer} km, petrol remaining {self.__tank} litres'

    def fill_up(self): 
        self.__tank = 60

    def drive(self, distance):
        
        if self.__tank >= distance:
            self.__odometer += distance
            self.__tank -= distance
        else:
            self.__odometer += self.__tank
            self.__tank = 0

if __name__ == "__main__":
    car = Car()
    print(car)
    car.fill_up()
    print(car)
    car.drive(20)
    print(car)
    car.drive(50)
    print(car)
    car.drive(10)
    print(car)
    car.fill_up()
    car.fill_up()
    print(car)

