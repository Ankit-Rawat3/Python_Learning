def is_armstrong(number):
    # Convert the number to a string to iterate over its digits
    num_str = str(number)
    num_digits = len(num_str)  # Get the number of digits

    # Sum of each digit raised to the power of the number of digits
    total = sum(int(digit) ** num_digits for digit in num_str)

    # Check if the sum is equal to the original number
    return total == number


# Input from the user
num = int(input("Enter a number: "))

# Check if it's an Armstrong number
if is_armstrong(num):
    print(f"{num} is an Armstrong number.")
else:
    print(f"{num} is not an Armstrong number.")
