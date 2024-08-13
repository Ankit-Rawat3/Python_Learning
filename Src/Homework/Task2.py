#write a program to take two user input and find max, pow(n1,n2), sub,mul,sum,div
# and format output with f{""}

N1=int(input("Enter Number 1: "))
N2=int(input("Enter Number 2: "))

print("Maximum of "f"{N1} and "f"{N2} is ", max(N1,N2))
print("Power of "f"{N1} to "f"{N2} is", pow(N1,N2))
print("Subtraction of "f"{N1} from "f"{N2} is", N1-N2)
print("Sum of "f"{N1} with "f"{N2} is", N1+N2)
print("Multiplication of "f"{N1} to "f"{N2} is", N1*N2)
print("Div of "f"{N1} to "f"{N2} is", N1/N2)


