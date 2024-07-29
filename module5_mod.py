class NumberProcessor:
    def __init__(self):
        self.numbers = []

    def add_number(self, number):
        self.numbers.append(number)

    def find_number(self, x):
        try:
            index = self.numbers.index(x)
            return index + 1  # Return 1-based index
        except ValueError:
            return -1
