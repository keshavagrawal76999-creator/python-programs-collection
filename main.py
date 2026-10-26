def factorial(n):
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers.")
    result = 1
    for value in range(2, n + 1):
        result *= value
    return result


def fibonacci(count):
    if count < 0:
        raise ValueError("Count cannot be negative.")
    sequence = []
    a, b = 0, 1
    for _ in range(count):
        sequence.append(a)
        a, b = b, a + b
    return sequence


def is_prime(n):
    if n < 2:
        return False
    divisor = 2
    while divisor * divisor <= n:
        if n % divisor == 0:
            return False
        divisor += 1
    return True


def is_palindrome(text):
    cleaned = ''.join(char.lower() for char in text if char.isalnum())
    return cleaned == cleaned[::-1]


def main():
    print("Python Programs Collection")
    print("1. Factorial  2. Fibonacci  3. Prime check  4. Palindrome check")
    choice = input("Choose 1-4: ").strip()
    try:
        if choice == "1":
            print("Factorial:", factorial(int(input("Enter a non-negative integer: "))))
        elif choice == "2":
            print("Sequence:", fibonacci(int(input("How many numbers? "))))
        elif choice == "3":
            print("Prime:", is_prime(int(input("Enter an integer: "))))
        elif choice == "4":
            print("Palindrome:", is_palindrome(input("Enter text: ")))
        else:
            print("Please choose a number from 1 to 4.")
    except ValueError as error:
        print("Input error:", error)


if __name__ == "__main__":
    main()
