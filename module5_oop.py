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

def main():
    processor = NumberProcessor()

    n = int(input("Enter a positive integer N: "))
    for _ in range(n):
        number = int(input("Enter a number: "))
        processor.add_number(number)

    x = int(input("Enter a number to search (X): "))
    result = processor.find_number(x)
    
    print(result)

if __name__ == "__main__":
    main()
