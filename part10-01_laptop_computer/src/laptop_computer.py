# Write your solution here:
class Computer:
    def __init__(self, model: str, speed: int):
        self._model = model
        self._speed = speed

    @property
    def model(self):
        return self._model

    @property
    def speed(self):
        return self._speed

class LaptopComputer(Computer):

    def __init__(self, model: str, speed: int, weigth: int):
        super().__init__(model, speed)
        self._weigth = weigth

    def __str__(self):
        return f'{self._model}, {self._speed} MHz, {self._weigth} kg'

if __name__ == "__main__":
    laptop = LaptopComputer("NoteBook Pro15", 1500, 2)
    print(laptop)