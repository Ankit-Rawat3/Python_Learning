#WAP to compare two number if they are greater,smaller or eqaual to each other


num1=int(input("Enter the first Number "))
num2=int(input("Enter the Second Number "))

"""print("Number1 is greater than number2:",num1>num2)
print("Number1 is less than number2:",num1<num2)
print("Number1 is equal than number2:",num1==num2)
"""
#or
if(num1>num2):
    print("Number 1 is greater")
elif(num1<num2):
    print("Number 1 is Smaller")
else:
    print("Both numbers are equal")