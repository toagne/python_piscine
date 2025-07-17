class calculator:
    def __init__(self, numbers: list):
        self.numbers = numbers
    # decorator
    def dotproduct(V1: list[float], V2: list[float]) -> None:
        print(f'Dot product is: {sum([V1[i] * V2[i] for i in range(0, len(V1))])}')
    # decorator
    def add_vec(V1: list[float], V2: list[float]) -> None:
        print(f'Add Vector is: {[float(V1[i] + V2[i]) for i in range(0, len(V1))]}')
    # decorator
    def sous_vec(V1: list[float], V2: list[float]) -> None:
                print(f'Sous Vector is: {[float(V1[i] - V2[i]) for i in range(0, len(V1))]}')