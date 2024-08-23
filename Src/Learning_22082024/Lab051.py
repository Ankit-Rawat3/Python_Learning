def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        print(a)
        a, b = b, a + b

# Example: Print the first 10 Fibonacci numbers
fibonacci(7)