#WAp to find max between 3 numbers

num1=int(input("Enter the number1 :\n"))
num2=int(input("Enter the number2 :\n"))
num3=int(input("Enter the number3 :\n"))

if(num1>num2) and (num1>num3):
    print("num1 is greater")
elif(num2>num1) and (num2>num3):
    print("Num2 is greater")
else:
    print("Num3 is greater")

maximum=max(num1,num2,num3)
print("Maximum is",maximum)
