"""def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        print(a)
        a, b = b, a + b

# Example: Print the first 10 Fibonacci numbers
fibonacci(7)
"""

"or"

num_terms = int(input("Enter the number of terms in the Fibonacci series: "))
a,b=0,1

print("fabonacci series")
count=0
while count<=num_terms:
    print(a, end= ' ')

    a,b=b,a+b

    count=count+1