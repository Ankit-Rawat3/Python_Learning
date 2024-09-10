print("Start of program")
try:
    a= int(input("Enter num1"))
    b= int(input("Enter num2"))
    c=a/b

    print("Result Div is ", c)
except Exception as e:
    print(e)
    print("Please check your input, should not be string or zero")

print("End of program")
