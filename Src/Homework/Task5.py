#WAP to compare two number if they are greater,smaller or eqaual to each other


num1=int(input("Enter the first Number "))
num2=int(input("Enter the Second Number "))

"""print("Number1 is greater than number2:",num1>num2)
print("Number1 is less than number2:",num1<num2)
print("Number1 is equal than number2:",num1==num2)
"""
#or
if(num1>num2):
    print(f"{num1} is greater than {num2}")
elif num1<num2:
    print(f"{num1} is smaller than {num2}")
else:
    print(f"{num1} is equal to {num2}")