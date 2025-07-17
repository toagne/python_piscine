class calculator:
    def __init__(self, numbers: list):
        self.numbers = numbers

    def __add__(self, object) -> None:
        self.numbers = [number + object for number in self.numbers]
        print(self.numbers)
    def __mul__(self, object) -> None:
        self.numbers = [number * object for number in self.numbers]
        print(self.numbers)
    def __sub__(self, object) -> None:
        self.numbers = [number - object for number in self.numbers]
        print(self.numbers)
    def __truediv__(self, object) -> None:
        if object == 0:
            print('cannot divide by 0')
            return None
        self.numbers = [number // object for number in self.numbers]
        print(self.numbers)