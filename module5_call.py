from module5_mod import NumberProcessor

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
