def add_numbers(a, b):
    return a + b

def main():
    print("This is a simple adder program.")
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    result = add_numbers(a, b)
    print("The sum is:", result)

if __name__ == "__main__":
    main()
