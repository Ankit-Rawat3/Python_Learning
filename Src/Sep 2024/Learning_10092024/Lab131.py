#try ,except, finally

try:
    a= int(input("Enter num1 \n"))
    b= int(input("Enter num2 \n"))
    c=a/b
except ValueError as ve:
    print(ve)
except ZeroDivisionError as zde:
    print(zde)
else:
    print(f"Result is {c}")
finally:
    print("Program ended")
